from bs4 import BeautifulSoup
import urllib2
import pprint

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
<<<<<<< HEAD
		if "vegetarian" not in i and "vegan" not in i:
=======
		if ("vegetarian" not in i) and ("vegan" not in i):
>>>>>>> Fix vegetarian functionality
			output_list.remove(i)
	return output_list

def get_all_meals(url):
	url = urllib2.urlopen(url)
	content = url.read()
	soup = BeautifulSoup(content)
	# print soup
	headers_raw = soup.findAll("h4")
	# print headers
	table_content = soup.findAll("table", {"class": "contentpaneopen"})
	# content = table_content[1].findAll("li")
	all_dict = {}
	for raw_header in headers_raw:
		header_title = raw_header.getText()
		temp = {}
		for category in raw_header.next_sibling.findAll("strong"):
			categoryText = category.getText()
			temp[categoryText] = listify(category)
		all_dict[header_title] = temp
	return all_dict

def get_veg_meals(url):
	url = urllib2.urlopen(url)
	content = url.read()
	soup = BeautifulSoup(content)
	# print soup
	headers_raw = soup.findAll("h4")
	# print headers
	table_content = soup.findAll("table", {"class": "contentpaneopen"})
	# content = table_content[1].findAll("li")
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
pp.pprint(get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html"))

<<<<<<< HEAD
# print all_dict["BRUNCH"]["Pizza"]

# pp.pprint(veg_dict) "http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html"
=======
pp.pprint(veg_dict)
>>>>>>> Fix vegetarian functionality
