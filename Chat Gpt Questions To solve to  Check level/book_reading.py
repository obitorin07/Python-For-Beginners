#!/usr/bin/env python3
# i ask chatgpt to give me questions to solve

"""
👇 Question

Write a Python program that prompts
the user to enter the number of books they want to read over the next month.
If the entered number is between 5 and 15 (inclusive), 
ask for the titles of the books one by one using a loop, 
and after each title, display the message "[title] added to your reading list." 
If the entered number is less than 5, 
print "You should aim to read more!" If the entered number is 15 or higher, 
print "That's an ambitious goal!".
"""

ask_user = int(input("How Many Books You Want To Read over Next Month :"))
if ask_user>=5 and ask_user<15:
	for i in range(ask_user):
		book_title = input("Enter The Name of Title Book:")
		print("{} added to your reading list.".format(book_title))
elif ask_user<5:
	print("You Should aim to read more!")
else:
	print("That's an ambitious goal!")

