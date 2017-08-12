import csv
import requests
from bs4 import BeautifulSoup

athlete_number = 0;
id_number = 800;

while(id_number<820):
	
	url = "https://www.athletic.net/TrackAndField/Athlete.aspx?AID=4018" + str(id_number) + "#/L0"
	r = requests.get(url)

	soup = BeautifulSoup(r.content, 'html.parser')
	
	id_number += 1

	if soup.title is not None:
		file_name = "athlete" + str(athlete_number) + (".txt")
		athlete_number += 1
	
		title = str(soup.title.string)
		title = title.replace('\n','').replace('\t','').replace('\r','')
		athlete_name = title.split('-')[0]

		text_file = open(file_name, "w")
		text_file.write("Name: %s\n" % athlete_name)

		for event in soup.find_all('table', {"class" : "table table-sm histEvent"}):
			for event_name in event.find_all('h5', {"class" : "bold"}):
				text_file.write("Event: %s " % str(event_name.contents[0]))
			for event_time in event.find_all('a', {"class" : " PR"}):
				text_file.write("Time: %s\n" % str(event_time.contents[0]))
		
		text_file.close()

