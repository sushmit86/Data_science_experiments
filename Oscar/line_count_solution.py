from __future__ import  division

import urllib2



if __name__ == '__main__':
    print "Main Program Started"
    print "Don't Enter any key ,Reading data takes some time"
    try:
        target_url = "http://www2.census.gov/census_2000/datasets/PUMS/FivePercent/New_York/REVISEDPUMS5_36.TXT"
        data = urllib2.urlopen(target_url)
        req = requests.get(string)
        total_count = sum(1 for line in data)
        total_count_p = sum(1 for line in data if line.rstrip().startswith('p') or line.rstrip().startswith('P'))
        print total_count_p, total_count
        print "Ratio : " , round(total_count_p/total_count,2)
    except:
         print "Main Program Aborted"










