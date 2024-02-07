#!/usr/bin/env python3
"""Ask the user to enter 1, 2 or 3. If they enter a 1, display
the message “Thank you”, if they enter a 2, display
“Well done”, if they enter a 3, display “Correct”. If
they enter anything else, display “Error message”.
"""


print("Enter 1 or 2 or 3")
user_input =int(input("Enter The Numbers:"))
if user_input==1:
    print("Thank you")
elif user_input ==2:
    print("well done")
elif user_input==3:
    print("Correct")
else:
    print("Error")