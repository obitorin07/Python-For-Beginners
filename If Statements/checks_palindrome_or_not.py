#!/usr/bin/env python3

user_input = input("Enter The string you want to check is palindrome or not :").lower()

if user_input == user_input[::-1]:
    
    print(f"{user_input} Is palindrome")
else:
    print(f"{user_input} Not palindrome")