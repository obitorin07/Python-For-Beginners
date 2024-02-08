#!/usr/bin/env python3

"""Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case."""

first_name =input("Enter Your First Name:")
if len(first_name)<=5:
    last_name =input("Enter The Last Name:")
    print("Your Full Name is :",(first_name+last_name).upper())
    #i can do this like i declare new variable and concatenate both in that varibale
else  :
    print(first_name.lower())