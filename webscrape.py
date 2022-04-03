import csv
import requests
from bs4 import BeautifulSoup

with open('AtheleteLinks.csv', mode ='r')as file:

    linksFile = csv.reader(file)

    urlList = ["dummy",]
    numLines = 0
    
    for lines in linksFile:
            for links in lines:
                urlList.append(links)
            numLines += 1

urlList.remove("dummy")
while numLines > 1:
    urlList.remove('')
    numLines -= 1

for url in urlList:
	r = requests.get(url)

	soup = BeautifulSoup(r.content, 'html.parser')

	title = str(soup.title.string)
	title = title.replace('\n','').replace('\t','').replace('\r','')
	athlete_name = title.split('-')[0]
	
	file_name = str(athlete_name.strip()) + (".txt")
	
	text_file = open(file_name, "w")
	text_file.write("Name: %s\n" % athlete_name)

	for event in soup.find_all('table', {"class" : "table table-sm histEvent"}):
		for event_name in event.find_all('h5', {"class" : "bold"}):
			text_file.write(str(event_name.contents[0]) + ":")
		
		eventTimeList = ['Times:',]
		for times in event.find_all('a'):
			eventTimeList.append(times.string)
		currentValue = "NA"
		for input in eventTimeList:
			if 'PR' in input:
				break
			elif 'PR' not in input:
				currentValue = input
		
		text_file.write(' ' + currentValue + "\n")
	
	text_file.close()