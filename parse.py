from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse


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
    url = urllib.request.urlopen(url)
    content = url.read()
    soup = BeautifulSoup(content)
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
    url = urllib.request.urlopen(url)
    content = url.read()
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
