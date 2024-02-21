#!/usr/bin/env python3
"""Ask for the name of somebody the user wants to invite 
to a party. After this, display the message “[name] has 
now been invited” and add 1 to the count. Then ask if 
they want to invite somebody else. Keep repeating this 
until they no longer want to invite anyone else to the 
party and then display how many people they have 
coming to the party. """

again ='yes'
count =0
while again =='yes':
    invite=input("Enter Name of person you want to invite :")
    print(f"{invite} has been invited")
    count+=1
    #it is equivalent to count =count+1
    again =input("Do u want to invite any other peoples?:(yes/no)").lower()

print(f"{count} peoples are coming to party lets enjoy!")