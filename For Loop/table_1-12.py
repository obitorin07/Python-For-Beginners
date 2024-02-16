#!/usr/bin/env python3
"""Ask the user to enter a number between 1
and 12 and then display the times table for
that number"""
number = int(input("Enter Number 1 -12 :"))
if number <=12:
    for i in range(1,11):
        result = i *number
        #print(i,"x",number,"=",result)             this look very bad right while reading
        #print(f"{i} x {number} = {result} ")       this look little better right

        print("{1} x {0} ={2}".format(i,number,result))
        # this is outstanding for reading anyone can understand

else:
    print("print numbers between 1-12")
