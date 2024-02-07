#!/user/bin/env python3
"""Task the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the larger
number in a user-friendly format. """

over_100 =int(input("Enter The Number Over 100:"))
under_10 = int(input("Enter The Number Under 10:"))
answer =over_100//under_10

print(under_10,"goes into",over_100,"in",answer,"times")