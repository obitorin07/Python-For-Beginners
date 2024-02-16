#!/usr/bin/env python3
"""Change program
display_name.py to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered. """

name = input("Enter Name :")
numbers =int(input("Enter How Many TImes:"))
for _ in range(0,numbers):
    for i in name:
        print(i)