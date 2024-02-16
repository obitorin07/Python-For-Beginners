#!/usr/bin/env python3
"""Set a variable called total to 0. Ask the user to enter 
five numbers and after each input ask them if they 
want that number included. If they do, then add the 
number to the total. If they do not want it included, 
don’t add it to the total. After they have entered all five
numbers, display the total. """

#condition1 
total =0
for _ in range (0,5):
    number = int (input("Enter The Number"))
    response = input("Do You Want Add These Numbera? yes /no").lower()
   
    if response=="yes":
        total =total+number
print(total)