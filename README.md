My first proper script, ever -- a simple web scraper that I built using Python 2.7.6.

The script scrapes the new job listings from the Austin Community College jobs portal and stores the results in a CSV. I've set up a cron job to run the script once a day; when the script runs, it compares the data stored in the old CSV to the new results, and if there is a new listing, it overwrites the contents of the CSV. Then, if there are new listings, it sends me a text message notifying me that there is a new listing. 



