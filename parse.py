from bs4 import BeautifulSoup
import urllib2

url = urllib2.urlopen("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/1920-commons/1920-menu.html")
content = url.read()
soup = BeautifulSoup(content)
print soup
headers = soup.findAll("h4")
print headers
table_content = soup.findAll("table", {"class": "contentpaneopen"})
content = table_content[1].findAll("li")
print content
