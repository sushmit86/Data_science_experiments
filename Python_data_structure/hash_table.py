# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:08:24 2015

@author: sushmitroy
"""

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data =  [None]*self.size