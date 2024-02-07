#!/usr/bin/env python3
"""Ask for two numbers. If
the first one is larger
than the second, display
the second number first
and then the first
number, otherwise show
the first number first and
then the second."""

number_one = int(input("Enter The First Number:"))
number_two = int(input("Enter The Second Number :"))
if number_one>number_two:
    print(f"{number_one} is Bigger Than {number_two}" )

else:
    print(f"{number_two} is Bigger Than {number_one}")