#!/usr/bin/env python3
"""Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1)."""

fav_song =input("Enter 1st line of your fav song :")
#my fav is snapping one teo where you still in my heart..
print("The Length of character Of your fav song is ={} characters".format(len(fav_song)))
starting = int(input("Enter StartingLine Your want find:"))
ending= int(input("Enter Endline Line Your want find:"))
print(fav_song[starting:ending])
#this is used to find index
#use can do likethis also

print(fav_song[0:])