#!/usr/bin/env python3

"""Ask the user to enter a
number with lots of
decimal places. Multiply
this number by two and
display the answer."""



user = float(input("Enter Any Numbers With Decimal Value:"))
print(round((user*2)))
#round work as if user enter 25.5 it whill give 50 if user enter 25.60 it will show 51 because if under 5comes then remains same if over 5it will add 1 
