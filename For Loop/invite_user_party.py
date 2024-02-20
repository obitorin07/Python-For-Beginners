#!/usr/bin/env python3

""" 👇Question

Ask how many people the user wants to invite to a party. If they enter a number below 
10, ask for the names and after each name display “[name] has been invited”. If they 
enter a number which is 10 or higher, display the message “Too many people”."""


invite_users = int(input("How many Peoples You want to invite:")) 

#here checks condition if user enter below 10 then for loop ask user to
#which friend he/she want to invite number of times (invite_users)

if invite_users<10:
	for i in range(0,invite_users):
		name =input("Enter The Name of Your Friend you Want to invite:")
		print("{} has been invited ".format(name))
else:
	print("too many Peoples")
