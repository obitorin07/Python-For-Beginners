#!/usr/bin/env python3

"""This is first for loop to print 10 numbers"""
"""if i try to iterate direct user it will send an error int not iterable so i used range"""

user =int(input("How many Numers you want to iterate:"))
for k in range(user):
    print(k)