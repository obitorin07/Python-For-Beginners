#!/usr/bin/env python3
"""Ask the user to enter their first name and surname in lower 
case. Change the case to title case and join them together. 
Display the finished result."""

#i use directly built in lower()
first_name = input("Enter Your First Name:").lower()
last_name = input("Enter Your Last Name:").lower()
full_name =first_name+" "+last_name
change_case= first_name.title() +" "+ last_name.title()
print("With Lower Case :",full_name)
print("With Title Case:",change_case)
