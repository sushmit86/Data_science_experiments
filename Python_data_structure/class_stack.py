# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 05:38:22 2015

@author: sushmitroy
"""

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def pop(self):
        return self.items.pop()
    def push(self,item):
        return self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


def revstring(mystring):
    S = Stack()
    for i in mystring:
        S.push(i)
    revstr = ''
    while not(S.isEmpty()):
        revstr = revstr + S.pop()
    return revstr
    
    
def parchecker(symbolstring):
    mystack = Stack()
    balanced =True
    for index,par in enumerate(symbolstring):
        if par == ')' and mystack.isEmpty():
            balanced = False
        elif par == ')' and not(mystack.isEmpty()):
            mystack.pop()
        elif par == '(':
            mystack.push(par)
    if not(mystack.isEmpty()):
        balanced = False
    return balanced

def parcheckerGeneral(symbolstring):
    mystack = Stack()
    balanced = True
    for par in symbolstring:
        if (par ==')' or par =='}' or par == ']') and mystack.isEmpty():
            balanced = False
        elif (par =='(' or par =='{' or par == '['):
            mystack.push(par)
        elif (par == ')'):
            if mystack.peek()!= '(':
                balanced = False
            else:
                mystack.pop()
        elif (par == '}'):
            if mystack.peek()!= '{':
                balanced = False
            else:
                mystack.pop()
        elif (par == ']'):
            if mystack.peek()!= '[':
                balanced = False
            else:
                mystack.pop()

    if not(mystack.isEmpty()):
        balanced = False
    return balanced
    

#print(parcheckerGeneral('{{([][])}()}'))
#print(parcheckerGeneral('[{()]'))

def decimal_to_bin(dec_number):
    bin_stack = Stack()
    while (dec_number != 0):
        bin_stack.push(dec_number%2)
        dec_number = dec_number//2
    
    rev_str = ''
    while not(bin_stack.isEmpty()):
        rev_str = rev_str + str(bin_stack.pop())
    return rev_str
#print (decimal_to_bin(42))  
    
def decimal_to_base(dec_number,base):
    digits ='0123456789ABCDEF'
    base_stack = Stack()
    while(dec_number!= 0):
        base_stack.push(dec_number%base)
        dec_number =dec_number//base
    base_str =''
    while not(base_stack.isEmpty()):
        base_str = base_str + digits[base_stack.pop()]
    return base_str
#print(decimal_to_base(25,2))
#print(decimal_to_base(256,16))
    
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    Postlist = []
    tokenlist = infixexpr.split()
    alphabets  ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    for token in tokenlist:
        if token[0] in alphabets or token[0] in numbers:
            Postlist.append(token)
        elif token =='(':
            opstack.push(token)
        elif token ==')' :
            toptoken = opstack.pop()
            while toptoken != '(':
                Postlist.append(toptoken)
                toptoken = opstack.pop()
        else :
            while( not opstack.isEmpty() and prec[opstack.peek()] >= prec[token]):
                Postlist.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        Postlist.append(opstack.pop())
    
    return " ".join(Postlist)
#print(infixToPostfix("A * B + C * D"))
#print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
#print(infixToPostfix("( A + B ) * ( C + D )"))
#print(infixToPostfix("( A + B ) * C"))
#print(infixToPostfix("10 + 3 * 123456"))

def doMath(op,op1,op2):
    if op =='*':
        return op2*op1
    elif op=='/':
        return op1/op2
    elif op=='+':
        return op2+op1
    else:
        return op2 - op1
    
    

def postfixval(postfixExpr):
    operandstack = Stack()
    tokenlist = postfixExpr.split()
    numbers = "0123456789"
    for token in tokenlist:
        if token[0] in numbers:
            operandstack.push(int(token))
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = doMath(token,operand1,operand2)
            operandstack.push(result)
    return operandstack.pop()
#print(postfixval('7 8 + 3 2 + /'))

def infixToPrefix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    Pretlist = []
    tokenlist = infixexpr.split()
    tokenlist.reverse()
    alphabets  ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    for token in tokenlist:
        if token[0] in alphabets or token[0] in numbers:
            Pretlist.append(token)
        else:
            while(not opstack.isEmpty() and prec[opstack.peek()] > prec[token]):
                Pretlist.append(opstack.pop())
            opstack.push(token)
    while (not opstack.isEmpty()):
        Pretlist.append(opstack.pop())
    Pretlist.reverse()
    return "".join(Pretlist)
            
    
print(infixToPrefix("A + B * C + D / E"))
            
        
    
        

          
            
            
        


