#!/usr/bin/env python3
"""Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”."""

#here i used "capitalize " because i want user entered string into capitalize becauase i dont know
#some users can write like RED or red or Red or rEd or reD something like that
#so i dont want to give too much conditions in my if statement
# like user_fav_color =="RED" or like user_fav_color =="red" etc... like that that is reason i use


user_fav_color =input("Enter Your Favourite Color Name :").capitalize()
if user_fav_color =="Red":
    print(f"I like {user_fav_color} color Too")
else:
    print(f"i dont like {user_fav_color} color i prefer Red Color ")
