# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 01:58:52 2015

@author: sushmitroy
"""

class Polygon:
    def __init__(self,no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
       self.sides = [float(input("Enter Side " + str(i+1)+" : "))  for i in range(self.n)]
    def displaySides(self):
        for i in range(self.n):
            print ("The lenghth of side "+str(i+1)+"is :"+self.sides[i])
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print('The area of the triangle is %0.2f' %area)
    
        