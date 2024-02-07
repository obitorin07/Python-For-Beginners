<<<<<<< Updated upstream
#!/usr/bin/env python3\

=======
#!/bin/usr/env python3
>>>>>>> Stashed changes
year = int(input("Enter Year:"))
def find_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
<<<<<<< Updated upstream
        print("not leap")
=======
        print("Not Leap")
>>>>>>> Stashed changes
find_leap(year)
