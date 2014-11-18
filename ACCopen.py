import csv

def check_results():
	# Check the data to see if there are any new results
	with open('accresults.csv') as f:
		dfile = csv.DictReader(f, ("url", "closing date", "location", "title"), delimiter='|')
		for row in dfile:
			print row
		

check_results()


