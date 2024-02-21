#!/usr./bin/env python3
"""Create a variable called 
compnum and set the value 
to 50. Ask the user to enter a 
number. While their guess 
is not the same as the 
compnum value, tell them if 
their guess is too low or too 
high and ask them to have 
another guess. If they enter 
the same value as 
compnum, display the 
message “Well done, you 
took [count] attempts."""

secret_number =50
count =1
guess =int(input("Can You Guess The Secret Number:"))
while guess!=50:
    if guess <=50:
        print("Too Low")
    else:
        print("too high")
    guess =int(input("Have another guess"))
    count=count+1
print("well done you guessed it.{} is secret key. you took {} attempt to guess".format(secret_number,count))
    