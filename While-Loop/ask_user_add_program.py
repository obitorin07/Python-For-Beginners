#!/usr/bin/env python3
"""Ask the user to enter a 
number and then enter 
another number. Add these 
two numbers together and 
then ask if they want to add 
another number. If they 
enter “y", ask them to enter 
another number and keep 
adding numbers until they 
do not answer “y”. Once the 
loop has stopped, display 
the total. """
no1 =int(input("Enter The First Number:"))
total =no1
again ='yes'
while again =='yes':
    no2 =int(input("Enter The 2nd Number:"))
    total +=no2
    again = input("Do U want to add again ? (yes/no)").lower()
print("The Addition of {} {} = {}".format(no1,no2,total))
