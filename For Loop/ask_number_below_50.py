#!/usr/bin/env python3
"""Ask for a number below 50 and then count down from
50 to that number, making sure you show the number
they entered in the output. """

"""Method 1"""
# number =0
# while number<=50 :
#     number = int(input("Enter number Below 50:"))
#     for num in range(50,number-1,-1):
#         print(num)

"""Method 2"""

number = int(input("Enter number Below 50:"))

if number<=50:
    for num in range(50,number-1,-1):
        print(num)
else:
    print("Entered Number is Not Less than 50")