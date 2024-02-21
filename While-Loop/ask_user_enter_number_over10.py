#!/usr/bin/env python3
"""Ask the user to enter 
a number. Keep 
asking until they enter 
a value over 10 and 
then display the 
message “The last 
number you entered 
was a [number]” and 
stop the program."""

usr_input =0
while usr_input <=10:
    usr_input =int(input("Enter The Number :"))

print(f"The last number you entered was a {usr_input}")
    

