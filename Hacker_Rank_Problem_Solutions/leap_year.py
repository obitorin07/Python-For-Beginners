#!/bin/usr/env python3\

year = int(input("Enter Year:"))
def find_leap(year):
    if (year %4==0 and year %100!=0) or (year %400==0):
        print("leap year")
    else:
        print("not leap")
find_leap(year)