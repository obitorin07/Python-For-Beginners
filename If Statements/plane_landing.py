#!/usr/bin/env pyṭhon3
#im writting program just i watched one movie about airoplane landing so
# i thought  lets write code about situation when plane will be land

ask_adminstrator =input("Sir Please Tell Us There is runway is free or Not to land plane[free/NotFree]:").lower()

if ask_adminstrator =='free':
    print("Yes You can land plane")
    
elif ask_adminstrator == 'notfree':
    print("dont land plane")
else:
    print("something error in type")
    