from bs4 import BeautifulSoup
import requests
import grequests


def listify(n):
    """
    returns the food options for each category of food
    eg: for "Comfort" it might return
         ["onion rings", "bread", "cheese"]
    """
    raw = n.next_sibling.next_sibling.getText()
    output_list = raw.split("\n")
    output_list = [_f for _f in output_list if _f]
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
    output_list = [_f for _f in output_list if _f]
    for i in output_list:
        if ("vegetarian" not in i) and ("vegan" not in i):
            output_list.remove(i)
    return output_list


def get_all_meals(url):
    """
    Prints out a dictionary of all the meals.
    """
    # Opens the source of the url and soupifies it
    content = requests.get(url)
    return parse_content(content)

def get_all_meals_concurrent(urls):
    rs = (grequests.get(u) for u in urls)
    return list(map(parse_content, grequests.map(rs)))

def parse_content(content):
    """Parsing code shared by get_all_meals and get_all_meals_concurrent"""
    soup = BeautifulSoup(content.text)
    # Finds all tags with h4 (LUNCH, DINNER, etc)
    headers_raw = soup.findAll("h4")
    # Creates master vegetarian dictionary
    all_dict = {}
    # For loop to create veg_dict
    for raw_header in headers_raw:
        header_title = raw_header.getText()
        temp = {}
        # "strong" finds all the categories
        for category in raw_header.next_sibling.findAll("strong"):
            categoryText = category.getText()
            temp[categoryText] = listify(category)
        all_dict[header_title] = temp
    return all_dict


def get_veg_meals(url):
    """
    Prints out a dictionary of all the vegetarian meals.
    """

    # Opens the source of the url and soupifies it
    url = requests.get(url)
    content = url.text
    soup = BeautifulSoup(content)
    # Finds all tags with h4 (LUNCH, DINNER, etc)
    headers_raw = soup.findAll("h4")
    # Creates master vegetarian dictionary
    veg_dict = {}
    # For loop to create veg_dict
    for raw_header in headers_raw:
        header_title = raw_header.getText()
        temp = {}
        # "strong" finds all the categories
        for category in raw_header.next_sibling.findAll("strong"):
            categoryText = category.getText()
            temp[categoryText] = veg_listify(category)
        veg_dict[header_title] = temp
