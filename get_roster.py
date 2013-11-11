#!/usr/bin/python
from lxml import html
from urllib import urlopen
import pickle

def get_rosters():
	html_file=urlopen("http://msn.foxsports.com/foxsoccer/premierleague/teams")
	doc = html.parse(html_file).getroot()
	#converts relative links to absolute links
	doc.make_links_absolute()

	#Get links to roster by scraping table in page for ...
	#links containing 'roster'
	rosterlinks=[link for link in doc.xpath('//*[@class="teamLinksWrapper"]/div/a/@href')if link.find("roster")!=-1]
	html_file.close()
	return rosterlinks


def get_players(roster_url):
	html_file=urlopen(roster_url)
	doc = html.parse(html_file).getroot()
	team_name=roster_url[roster_url.find("teams/")+6:roster_url.find("/roster")]
	players=doc.xpath('//*[@class="fsiTmFrontRosterPlayerNameText"]/text()')
	for name in players: name.encode("ascii","ignore")
	print players
	return team_name,players

general_roster={}
def main():
	EPL_roster_links=get_rosters()
	for link in EPL_roster_links:
		team_info=get_players(link)
		general_roster[team_info[0]]=team_info[1]
	# print general_roster
	roster_file=open('rosters.json',"w")
	roster_file.write(str(general_roster))
	roster_file.close()

if __name__ == '__main__':
	main()