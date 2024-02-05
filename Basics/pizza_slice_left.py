#!/usr/bin/env python3
"""Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a friendly format"""

before_eat =int(input("Enter The Number of slices pizza you started with:"))
after_eat= int(input("How many slice do you eat?:"))
if after_eat<=before_eat:
    remaining_slices =before_eat-after_eat
    print("Before Eat Pizza Slices =",before_eat)
    print("The Remaining slices of pizza =", remaining_slices)
    if after_eat ==0:
        print("Why dont You Eat Anything ?")
    else:
        pass
else :
    print("Are You lost you mind how can it possible ? you had {} number of slices  and you are saying  you eat {} this much this is insane right go wash your face and enter again 😜😜😜".format(before_eat,after_eat))

#output
#Enter The Number of slices pizza you started with:10
#How many slice do you eat?:6
#The Remaining slices of pizza = 4
