#!/usr/bin/env python3
"""Ask the user to enter their first name and then ask them to 
enter their surname. Join them together with a space between 
and display the name and the length of whole name."""

first_name = input("Enter Your First Name:")
last_name = input("Enter Your Last Name:")
print(first_name ,"",last_name)
full_name =first_name + " " +last_name
print("The Length of character of {} {} is {}".format(first_name,last_name,len(full_name)))