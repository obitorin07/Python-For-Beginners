#!/bin/usr/env python3

#in this code how "end =''" print function work
#range function rules
#1 start stop step
# 0 ,10,2

user_input = int(input("Enter range :"))
for i in range (1,user_input+1):
    print(i,end="")

    #output
    #Enter range :5
    #12345