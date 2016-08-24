# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 18:09:44 2015

@author: sushmitroy
"""


def gcd(m,n):
    while m%n !=0:
        oldm =m
        oldn =n
        
        m=oldn
        n = oldm%n
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num) + "/"+ str(self.den)
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num *self.den    
        return (firstnum==secondnum)
    def __mul__(self,other):
        firstmul = self.num * other.num
        secondmul = self.den * other.den
        common = gcd(firstmul,secondmul)
        return Fraction(firstmul//common,secondmul//common)
    def __sub__(self,otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __truediv__(self,other):
        firstmul = self.num * other.den
        secondmul = self.den * other.num
        common = gcd(firstmul,secondmul)
        return Fraction(firstmul//common,secondmul//common)
    def __lt__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num *self.den    
        return (firstnum<secondnum)
    def __gt__(self,other):
        firstnum = self.num * other.den
        secondnum = other.num *self.den    
        return (firstnum>secondnum)
    
    
    
        
def main():
    f1 = Fraction(2,3)
    f2 = Fraction(3,5)
    print ("Subtraction of f1 and f2")    
    print(f1-f2)
    print("Div:")
    print(f1/f2)
    print("less than")
    print(f1<f2)
    print ("greater than")
    print(f1>f2)
main()

        
        



    
