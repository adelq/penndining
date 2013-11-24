from bs4 import BeautifulSoup
import urllib2
import pprint

url = urllib2.urlopen("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html")
content = url.read()
soup = BeautifulSoup(content)
# print soup
headers_raw = soup.findAll("h4")
# print headers
table_content = soup.findAll("table", {"class": "contentpaneopen"})
# content = table_content[1].findAll("li")


def listify(n):
	"""
	returns the food options for each category of food
	eg: for "Comfort" it might return
	     ["onion rings", "bread", "cheese"]
	"""
	raw = n.next_sibling.next_sibling.getText()
	output_list = raw.split("\n")
	output_list = filter(None, output_list)
	return output_list


def veg_listify(n):
	"""
	vegetarian version of listify
	returns the food options for each category of food
	eg: for "Comfort" it might return
	     ["onion rings", "bread", "cheese"]
	"""
	raw = n.next_sibling.next_sibling.getText()
	output_list = raw.split("\n")
	output_list = filter(None, output_list)
	for i in output_list:
		if "vegetarian" not in i or "vegan" not in i:
			output_list.remove(i)
	return output_list

all_dict = {}
for raw_header in headers_raw:
	header_title = raw_header.getText()
	temp = {}
	for category in raw_header.next_sibling.findAll("strong"):
		categoryText = category.getText()
		temp[categoryText] = listify(category)
	all_dict[header_title] = temp


veg_dict = {}
for raw_header in headers_raw:
	header_title = raw_header.getText()
	temp = {}
	for category in raw_header.next_sibling.findAll("strong"):
		categoryText = category.getText()
		temp[categoryText] = veg_listify(category)
	veg_dict[header_title] = temp

# print all_dict
pp = pprint.PrettyPrinter(indent = 2)
pp.pprint(all_dict)

print all_dict["BRUNCH"]["Pizza"]

pp.pprint(veg_dict)