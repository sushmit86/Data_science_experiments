# Sushmit Roy -- sushmit86@gmail.com
import requests
import sys
import os
from bs4 import BeautifulSoup
from collections import OrderedDict
import json

# Set the current director
def set_current_dir():
    curr_dir = os.getcwd()
    sys.path.append(curr_dir)

# reads the URL and returns the BeautifulSoup object
def read_url(string):
    try:
        req = requests.get(string)
        soup = BeautifulSoup(req.content)
        return soup
    except:
          print "Could not read URL" + string
          return IOError

# generating the dict json
def generate_json_dic(soup):
    dict_json = {}  # dict to generate json
    list_elem = []
    dict_json['company_listing'] = list_elem
    table = soup.find('table', 'table table-hover')  # reading the table
    for a in table.findAll('a', href=True):  # iterating over the inner URL
        url_inner = "http://data-interview.enigmalabs.org" + a['href']
        soup_inner = read_url(url_inner)
        table_data = [[cell.text for cell in row("td")] for row in soup_inner("tr")]
        json_str = OrderedDict(table_data)
        list_elem.append(json_str)
    return dict_json

# generating the json file
# if file present , overwrites
def  write_json(file_name,dict_json):
    output = open(file_name, 'w+')
    json.dump(dict_json,output)
    output.close()
# Main function
if __name__ == '__main__':
    print "Main Program Started"
    try:
        set_current_dir() # set current directory
        url = "http://data-interview.enigmalabs.org/companies/"
        soup = read_url(url)  # read the URL
        dict_json = generate_json_dic(soup)  # Generate the json object
        write_json("solution.json", dict_json)  # write the json file
    except:
        print "Main Program Aborted"



