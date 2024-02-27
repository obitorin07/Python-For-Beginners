#!/usr/bin/env python3
"""Static program"""
# =============================================================================
# airline="AirIndia"
# luggage_weight=28
# AI_weight_limit=30
# EM_weight_limit=35
# if(airline=="AirIndia"):
#     if(luggage_weight<=AI_weight_limit):
#         print("Check-in cleared")
#     else:
#         print("Remove some luggage and come back")
# elif(airline=="Emirates"):
#     if(luggage_weight<=EM_weight_limit):
#         print("Check in cleared")
#     else:
#         print("Remove some luggage and come back")
# else:
#     print("Invalid airline")
# 
# =============================================================================

"""dyanamic program """
    
airline =input("Choose Airline from below menu :\n1.AirIndia\n2.Emirates {hint : just type (1/2)}:")

air_india_weight_limit =30
emirates_weight_limit=35

if airline=='1' or airline =='2':
    luggage_weight =int(input("Enter The laggage Weight: "))
    if airline=='1':
        if luggage_weight<=air_india_weight_limit:
            print("checkin is cleared")
        else:
            print("Remove some luggage and comeback")
    elif airline=='2':
        if emirates_weight_limit >=luggage_weight:
            print("checkin in cleared")
            
        else:
            print("Remove some luggage and comeback")
    
else:
    print("entered airline is invalid ")
            



