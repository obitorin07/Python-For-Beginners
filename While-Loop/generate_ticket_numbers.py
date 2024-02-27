#!/usr/bin/env python3
"""static program"""
# =============================================================================
# no_of_passengers=3
# ticket_number=1001
# print("Ticket Numbers for all the Passengers:")
# while(no_of_passengers>0):
#     print("T -",ticket_number)
#     ticket_number=ticket_number+1
#     no_of_passengers=no_of_passengers-1
# 
# 
# =============================================================================
"""Dynamic program"""

number_of_passengers =int(input("How Many passengers are travelling :"))

#ticket number start from 12000001 [8 digit number]
ticket_number =12000001
print("Ticket Number For All The passengers")

while number_of_passengers>0:
    print("ticket number is T-{}".format(ticket_number))
    ticket_number=ticket_number +1
    number_of_passengers =number_of_passengers-1