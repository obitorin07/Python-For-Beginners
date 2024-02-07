#!/usr/bin/env python3

"""Ask the user to enter a
number that is under
20. If they enter a
number that is 20 or
more, display the
message “Too high”,
otherwise display
“Thank you”. """

user_input= int(input("Enter The Value less than 20:"))
if user_input>=20:
    print("Too High")
else:
    print("Thank You")