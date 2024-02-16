#!/usr/bin/env python3
"""Ask the user to enter their 
name and a number. If the 
number is less than 10, then 
display their name that 
number of times; otherwise 
display the message “Too 
high” three times. """

name = input("Enter The Name:")
number = int(input("Enter The Number Less Than 10:"))
#condition1
if number<=10:
    for _ in range(number):
        print(name)
#condition2
else:
    for _ in range(0,3):
        print("Too High !")