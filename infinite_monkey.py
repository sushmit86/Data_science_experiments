# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Infinit Monkey problem
import random
def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res =""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res


def score(goal,teststring):
    numsame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
             numsame = numsame +1
    return numsame/len(goal)
 

def main():
    goalstring = "methinks it is like a weasel"
    newstring = generateOne(len(goalstring))
    best = 0
    newscore  = score(goalstring,newstring)
    while (newscore < 1):
        #print (newstring)        
        if (newscore > best):
            best = newscore
            print(newscore)
            print (newstring)
            best = newscore
        newstring = generateOne(len(goalstring))
        newscore = score(goalstring,newstring)
        
    
main()
