#!/usr/bin/env python3

"""Ask the user for their name and their age. Add 1 to their age
and display the output [Name] next birthday you
will be [new age]. """

user_name = input("what is your name dear :")
user_age = int(input("what is your age :"))
new_age = user_age+1
print("{} Your Next Birthay you will became {} year old ".format(user_name,new_age))

"""The Output
what is your name dear :obito
what is your age :15
obito Your Next Birthay you will became 16 year old """

