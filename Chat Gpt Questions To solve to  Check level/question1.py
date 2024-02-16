#!/usr/bin/env python3

""" Can you write a Python function that takes two parameters, a and b, and returns their sum?"""

def sum(a ,b):
    result = a+b
    return "The Sum of {} {} is {}".format(a,b,result)
a =int(input("1st num:"))
b=int(input("2nd num:"))
print(sum(a,b))