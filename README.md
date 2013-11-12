NLP_IE_football
===============

Information extraction project for Natural Language Processing (Info 256) - We will extract game details from reports like this http://espnfc.com/us/en/report/367471/report.html?soccernet=true&amp;cc=5901


INSTRUCTIONS
1. get_reports.py should be run to get the list of match report URLs, which are saved into 'report_links.txt' on separate lines. 
2. scraper.py should then be run to iterate through the 'report_links.txt' file and load each URL and then scrape for title and raw text of the report. Each report is saved in the 'reports' folder as:
	title+"_raw.txt
	e.g "Adam sinks Canaries_raw.txt"
3. run parsing and IE scripts on this raw text corpus (TBD)

##
Scraper takes html file and pulls out the text and saves it to a file of the same name + "_raw.txt"

##
