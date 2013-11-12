#!/usr/bin/python
from lxml import html
from urllib import urlopen
import pickle

#global variables
seed_url="http://espnfc.com/scores/_/league/eng.1/barclays-premier-league?cc=5901"
report_links=[]
num_of_reports=200


def get_reports(url):
	'''Using espnfc.com, scrape league scores page for reports'''
	global report_links
		
	
	html_file=urlopen(url)
	doc = html.parse(html_file).getroot()
	
	#converts relative links to absolute links
	doc.make_links_absolute()

	#Get links to reports by scraping table in page for ...
	#links containing 'report'
	report_links+=[link for link in doc.xpath('//*[@class="scores-links"]/a/@href')if link.find("report.html")!=-1]
	html_file.close()

	#recursively get more report links from score pages until num_of_reports
	if len(report_links)<=num_of_reports:
		
		#xpath for previous day of score page
		new_score_page=doc.xpath('//*[@class="game-dates"]/li/a/@href')[0]
		# print new_score_page
		print str(len(report_links))
		
		get_reports(new_score_page)

	return report_links





def main():
	reports_file=open("report_links.txt","w")
	for link in get_reports(seed_url):
		reports_file.write(link+"\n")
	reports_file.close()

if __name__ == '__main__':
	main()