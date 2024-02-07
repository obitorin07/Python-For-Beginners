#!/usr/bin/env python3

#exceptional handling
try :
    a = int (input("Enter The 1st Number :"))
    b = int (input("Enter The 2nd Number :"))
    result = a/b
    print("Result=",result)
except ZeroDivisionError:
    print("Division By Zero")
else:
    print("Successful Division")


