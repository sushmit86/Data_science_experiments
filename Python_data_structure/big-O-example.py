# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:38:04 2015

@author: sushmitroy
"""

import time
from random import randrange
def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin


def findMin1(alist):
    minsofar = alist[0]
    for i in alist[1:]:
        if i < minsofar:
            minsofar = i
    return minsofar
    


for listsize in range(1000,10001,1000):
    alist = [randrange(10000) for x in range(listsize)]
    start = time.time()
    print(findMin1(alist))
    end = time.time()
    print ("Size %d time %f" %(listsize,end-start))