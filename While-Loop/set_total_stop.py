#!/usr/bin/env python3
#QUESTION👇

"""Set the total to 0 to start with. While the total is 50 or less, ask 
the user to input a number. Add that number to the total and 
print the message “The total is… [total]”. Stop the loop when 
the total is over 50."""

total =0
while total <50:
    usr_input=(int(input("Enter The Number:")))
    total =total+usr_input
    print("Entered Number Is Not Satisfied")
    
print("The Total Is =",total)
