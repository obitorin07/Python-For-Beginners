#!/usr/bin/env python3
"""Alter program display_name.py so that it will ask the user to enter their
name and a number and then display their name that
number of times. """

name = input("Enter The Name:")
how_many_times = int(input("Enter How many times do you want to display:"))
for i in range(0,how_many_times):
    print(name)