from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
import smtplib

BASE_URL = ("http://www5.austincc.edu/ehire/posting/")

def parse_data(URL):
	# Parse results and insert into a list of dictionaries
	results = []
	soup = BeautifulSoup(urlopen(URL).read())
	rows = soup.find('table', 'border').find_all('tr', 'row_new')
	for row in rows:
		url = URL + row.a['href']
		title = row.find_all('strong')[1].get_text()
		location = row.find_all('td')[2].get_text()
		close_date = row.find_all('td')[3].get_text()
		results.append({"url": url, "title": title, "location": location, \
			"close date": close_date})


	# Open old CSV	
	with open('accresults.csv') as f:
		dlist = []
		dfile = csv.DictReader(f, ("url", "close date",\
		 "location", "title"), delimiter='|')
		for row in dfile:
			dlist.append(row)


	# Check to see if there are any new jobs
	if dlist[1] == results[1]:
		print "No new results"
	else:
		print "new results"
		record_results(results)
		new_results_notifcation()


def record_results(write_data):

	# Record results into a csv with dictionary keys as headers
	fields = write_data[0].keys()
	with open('accresults.csv', 'w') as f:
		dfile = csv.DictWriter(f, fieldnames=fields, delimiter='|')
		#dfile.writeheader()
		dfile.writerows(write_data)
	return write_data

def new_results_notifcation():

	# Sends an SMS notification saying there is a new listing
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('<email address>', '<password>')
	server.sendmail('<FROM ADDRESS>', '<TO ADDRESS>', 'There is a new job listing! Check it out!')
	server.quit()


parse_data(BASE_URL)
