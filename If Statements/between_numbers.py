#!/usr/bin/env python3
"""Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”. """
user_input =int(input("Enter The Number Between 10 to 20:"))
if user_input>=10 and user_input<=20:
    print("Thank you")
else:
    print("incorrect")