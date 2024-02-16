#!/usr/bin/env python3
"""Can you write a Python function that checks whether a given number is even or odd? Feel free to write the code"""
# def even_odd(number):
#     if number %2==0:
#         print(f"{number} Even")
#     else:
#         print(f"{number} Odd")
#
# number = int(input("Enter The Value:"))
# print(even_odd(number))

#this code inmplicitly return nono


def even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

number = int(input("Enter the value: "))
print(even_odd(number))
