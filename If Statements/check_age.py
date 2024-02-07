#!/usr/bin/env python3
"""Ask the user’s age. If they
are 18 or over, display the
message “You can vote”, if
they are aged 17, display the
message “You can learn to
drive”, if they are 16, display
the message “You can buy a
lottery ticket”, if they are
under 16, display the
message “You can go Trick or-Treating"""


user_age = int(input("Enter Your Age :"))
if user_age>=18:
    print("You Can Vote ")
elif user_age==17:
    print("You Can Learn To Drive")
elif user_age==16:
    print("You can Buy a lottery ticket")
else:
    print("You can go Trick Or treating")
