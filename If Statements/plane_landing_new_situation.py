#!/usr/bin/env python3
ask_adminstrator =input("Sir Please Tell Us There is runway is free or Not to land plane. or fuel is low?[free/low]:").lower()

if ask_adminstrator =='free':
    print("Yes You can land plane")
    
elif ask_adminstrator == 'low':
    print("Emergency landing ")
else:
    print("Circle in the air")
    