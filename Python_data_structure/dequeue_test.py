# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 00:07:04 2015

@author: sushmitroy
"""

class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def addFront(self,item):
        return self.items.append(item)
    def addRear(self,item):
        return self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
        
def palindrome_test(mystr):
    revstring = mystr[::-1]
    return mystr == revstring

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    flag = True
    while(chardeque.size()>1 and flag):
        first = chardeque.removeFront()
        last =  chardeque.removeRear()
        if first !=last:
            flag = False
    return flag
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
    