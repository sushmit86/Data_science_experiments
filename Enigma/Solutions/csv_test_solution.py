# Sushmit Roy -- sushmit86@gmail.com
import csv
import re
import sys
import os
import urllib
import urllib2
import datetime


# Setting python directory to present working directory(pwd) and returning path directory
def set_current_dir():
    curr_dir = os.getcwd()
    sys.path.append(curr_dir)
    return curr_dir

# downloading files test.csv and state_abbreviations.csv
# if test.csv and state_abbreviations.csv present then overwrites
def download_files(dir_name):
    url_common = 'https://s3.amazonaws.com/data-code-test/'
    list_files = ['test.csv', 'state_abbreviations.csv']

    for file_name in list_files:
        url = url_common + file_name
        file_path = dir_name + '/' + file_name
        try:
            urllib2.urlopen(url)  # to check if its a valid download
            urllib.urlretrieve(url, file_path) # downloading file and saving
        except IOError:
            print "Error downloading " + file_name
            print "Aborting program"
            raise IOError


# Procedure for cleaning string
def string_cleaning(string):
    return re.sub('\s+', ' ', string).strip()  # Also stripping any trailing spaces


# Procedure to return dict with state abbreviation(key) and state name(value)
def file_to_dict(file_name):
    read_file = open(file_name, 'rb')
    reader = csv.DictReader(read_file)
    state_abb_dict = {}
    for row in reader:
        state_abb_dict[row['state_abbr']] = row['state_name']
    read_file.close()
    return state_abb_dict
# Procedure to swap abbreviation with name
def code_swap(state_abbv_dict,state_abbv):
    if state_abbv in state_abbv_dict:
        return state_abbv_dict[state_abbv].strip()
    else:
        return "Not Mapped"
# Procedure to covert a string in format '%Y-%m-%d' to isoformat
def convert_date_iso(str_date):
    try:
        return datetime.datetime.strptime(str_date, '%Y-%m-%d').date().isoformat()
    except:
        return "Invalid date"

# Procedure to return iso fomat date if start_date is valid
def date_offset(start_date):
    months_choices = ''
    pattern1 = r"(\d{1,2})([/])(\d{1,2})([/])(\d{4})"  # MM/DD/YYYY pattern
    pattern2 = r"(\d{4})([-])(\d{1,2})([-])(\d{1,2})"  # YYYY-MM-DD pattern
    months_choices = ''
    for i in range(1, 13):
        if i != 12:
             months_choices = months_choices + r'\b' + datetime.date(2015, i, 1).strftime('%B') + r'\b|'
        else:
             months_choices = months_choices + r'\b' + datetime.date(2015, i, 1).strftime('%B') + r'\b'
    pattern3 = "(" + months_choices + ")" + r"(\s+)(\d{1,2})(\,\s+)(\d{4}\b)" # Monthname day,YYYY pattern
    # Check which pattern is present
    pattern1_searchObj = re.search(pattern1, start_date)
    pattern2_searchObj = re.search(pattern2, start_date)
    pattern3_searchObj = re.search(pattern3, start_date)

    if pattern1_searchObj != None:
        str_date = pattern1_searchObj.group(5) + '-' + pattern1_searchObj.group(1) + '-' + pattern1_searchObj.group(3)
        return convert_date_iso(str_date)
    elif pattern2_searchObj!= None:
        str_date = pattern2_searchObj.group(1) + '-' + pattern2_searchObj.group(3) + '-' + pattern2_searchObj.group(5)
        return convert_date_iso(str_date)
    elif pattern3_searchObj != None:
        month_str = datetime.datetime.strptime(pattern3_searchObj.group(1), '%B').strftime('%m')
        str_date = pattern3_searchObj.group(5) + '-' + month_str + '-' + pattern3_searchObj.group(3)
        return convert_date_iso(str_date)
    else:
        return "Invalid Date"

# writing solution.csv to present working directory
# if solution.csv is present , then overwrites
def write_solution():
    try:
        read_file = open('test.csv', 'rb')  # Reading file
        write_file = open("solution.csv", 'wb')  # Opening file
        reader = csv.reader(read_file)
        headers = reader.next()  # Getting header for test.csv
        headers.append('start_date_description')
        writer = csv.DictWriter(write_file, fieldnames=headers)
        writer.writeheader()
        state_abb_dict = file_to_dict("state_abbreviations.csv")
        for row in reader:
            temp_dict = {headers[i]: row[i] for i in range(len(headers)-1)}   # dictionary comprehension
            temp_dict['bio'] = string_cleaning(temp_dict['bio'])  # Cleaning Bio field
            temp_dict['state'] = code_swap(state_abb_dict, temp_dict['state'])  # State abbreviation with name
            temp_dict['start_date_description'] = date_offset(temp_dict['start_date'])   # date offset operation
            writer.writerow(temp_dict)
        read_file.close()   # closing file
        write_file.close()  # closing file

    except:
        read_file.close()  # closing file
        write_file.close()  # closing file
        raise IOError


# Main function
if __name__ == '__main__':
    try:
        print "Main Program started"
        curr_dir = set_current_dir()
        download_files(curr_dir) # download files
        write_solution()  # write solution
        print "solution.csv created"
        print "Main Program completed"
    except:
        print "Main Program Aborted"
# Executing Main Program

