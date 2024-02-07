#!/usr/bin/env python3
"""
Write a program
that will ask for a
number of days
and then will
show how many
hours, minutes
and seconds are
in that number of
days."""

print("Check Days,Hours,Seconds Calculator")
days =int(input("Enter How Many Days :"))
print("-----------------------------------")
hours =days *24
minutes = hours *60
second = minutes*60

print(f"In {days} Days There Are ")
print(f"{hours} Hours")
print(f"{minutes} Minutes")
print(f"{second} Seconds")