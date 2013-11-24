from bs4 import BeautifulSoup
import urllib2

url = urllib2.urlopen("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/1920-commons/1920-menu.html")
content = url.read()
soup = BeautifulSoup(content)
# print soup
headers = soup.findAll("h4")
# print headers
table_content = soup.findAll("table", {"class": "contentpaneopen"})
# content = table_content[1].findAll("li")

lunch_raw = headers[0].next_sibling
dinner_raw = headers[1].next_sibling
brunch_raw = headers[2].next_sibling

lunch = {}
lunchcats = lunch_raw.findAll('strong')


def listify(n):
	"""
	returns the food options for each category of food
	eg: for "Comfort" it might return
	     ["onion rings", "bread", "cheese"]
	"""
	raw = n.next_sibling.next_sibling.getText()
	output_list = raw.split("\n")
	output_list.pop()
	return output_list



bob = []
for category in lunchcats:
	categoryText = category.getText()
	lunch[categoryText] = listify(category)

print lunch












# print dinner_raw


# def dictify(ul):
#     result = {}
#     for i in ul.find_all("li", recursive=False):
#         key = next(i.stripped_strings)
#         ul = i.find("ul")
#         if ul:
#             result[key] = dictify(ul)
#         else:
#             result[key] = None
#     return result

# ul = soup.find("div", {"id": "accordion1"})
# print ul