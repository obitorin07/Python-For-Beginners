#!/usr/bin/env python3

age = int(input("Enter your Age:"))

try:
    if 18 < age <= 80:
        print("You Can Vote")
    else:
        print("You cannot Vote")

except ValueError:
    print("Not An Interger")
