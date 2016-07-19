
"""

@author: sushmitroy
"""

import sys
import urllib,urllib2
import os
import pandas as pd
import glob
import itertools
import time


## Setting python directory to pwd
def set_current_dir():
    curr_dir = os.getcwd()
    sys.path.append(curr_dir)
    
## Creating input and output  directory 
def create_input_output_dir():
    curr_dir = os.getcwd()
    input_dir_path = curr_dir+'/'+'input'
    if not os.path.exists(input_dir_path):
        os.makedirs(input_dir_path)
    output_dir_path = curr_dir+'/'+'output'
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    return input_dir_path
# solution for question 1
## downloading files if error prints the Year where error encountered
def download_files(start_year,end_year,input_path):
    print "Starting to download files. This step may take some time"
    print "Do not enter any Key"
    url_part1 = 'https://s3.amazonaws.com/dd-interview-data/data_scientist/baseball/appearances/'
    url_part3 = '-0,000'
    year_file = start_year
    while(year_file <=end_year ):
        url= url_part1 + str(year_file) + '/'+str(year_file)+url_part3
        input_file_path = input_path + '/' + str(year_file) + '.csv'
        try:
            urllib2.urlopen(url)  # to check if its a valid download
            urllib.urlretrieve(url,input_file_path)
            year_file = year_file + 1
        except IOError:
            print "Error downloading " + str(year_file)
            print "Ending operation here "
            raise IOError 
    print "All files downloaded "

###  read all downloaded csv and create a consolidated data frame
## return a pandas data frame 

def read_files(input_path):
    allFiles = glob.glob(input_path + "/*.csv")
    col_names = ['Year','Team','League','Player ID','Player Name']
    df_consolidated = pd.DataFrame() # Create empty pandas data frame
    for file_ in allFiles:
        df_csv = pd.read_csv(file_, header=None,index_col=False)
        df_first_five=df_csv.ix[:,0:4]
        df_consolidated=df_consolidated.append(df_first_five,ignore_index = True)
    df_consolidated.rename(columns={0: col_names[0], 1: col_names[1],2: col_names[2],3: col_names[3],4: col_names[4]}, inplace=True)
    return df_consolidated

# solution for question (2)
# returns a list with each element as Tuple
# T : Time complexity S:Space Complexity
# Let n -- Total Size of concatenated data 
# Let m -- Total teams
# Let p -- Total players
def create_triples(df_consolidated):
    start = time.time()
    dict_consolidated = df_consolidated.to_dict() # T : O(1)  S: O(n)
    # Creating a dictionary of team[key] & Players
    dict_team_player = {}
    for i in range(len(dict_consolidated['Team'])): #T:O(n) S:O(n)
         if dict_consolidated['Team'][i] not in dict_team_player:
                dict_team_player[dict_consolidated['Team'][i]] = {dict_consolidated['Player ID'][i]}
         else:
            dict_team_player[dict_consolidated['Team'][i]].add(dict_consolidated['Player ID'][i])
    list_tripe_pair =[]    
    for list_3 in list(itertools.combinations(list(set(df_consolidated['Team'].tolist())),3)): # T: O(m^3)  #S:O(m^3)
        if len(dict_team_player[list_3[0]]& dict_team_player[list_3[1]] & dict_team_player[list_3[0]]) >=50: # T: O(p)
                list_tripe_pair.append(list_3)
        
    end = time.time()
    print "Total execution time in sec for q2" 
    print round(end - start,2)
    return list_tripe_pair


# Solution for question 3
# Return type  Pandas Data Frame
def create_top_100(df_consolidated):
    df_grouped=df_consolidated.groupby(['Player ID','Player Name'])['Year'].nunique().reset_index()
    df2_sorted_100 = df_grouped.sort_values(['Year','Player Name'],ascending=[False,True],inplace=False).reset_index(drop = True)[0:100]
    df_name_year = df2_sorted_100[['Player Name','Year']]
    name_year_list = [tuple(x) for x in df_name_year.values]
    return name_year_list

# To write the output lists to file in output folder
def write_output(list_items,file_name):
    file_path = "output/" + file_name
    outfile = open(file_path,"w")
    for item in list_items:
        outfile.write(str(item))
        outfile.write('\n')
    outfile.close()
        
    

def main():
	try:
	    print "Main prog Started"
	    start_time = time.time()
	    set_current_dir() # Setting python Current directory to Pwd
	    input_dir_path=create_input_output_dir()  
	    download_files(1871,2014,input_dir_path)
	    df_consolidated=read_files(input_dir_path)    
	    write_output(create_triples(df_consolidated),"sol2.txt")
	    write_output(create_top_100(df_consolidated),"sol3.txt")
	    end_time = time.time()
	    print "Main prog Ends. Total time taken in sec: "
	    print round(end_time - start_time,2)
	    print "Answer for q1: Check input folder"
	    print "Answer for q2 and q3: Check output folder"
	except :
		print "Main Prog Aborted"

main()