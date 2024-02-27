#!/usr/bin/env python3
    
"""When you want to repeatedly execute a statement as long as a condition is met, 
    you can use the iteration statement called as while loop."""

print("The flight has landed")
print("Immigration check done")
print("Collect the baggage from the conveyor belt")
Baggage_Count=150
while Baggage_Count>=0:
    
    number_of_baggage_picked =int(input("Enter The Number of baggage picked :"))
    Baggage_Count=Baggage_Count-number_of_baggage_picked
    
    print('baggages are left to pick ' + str(Baggage_Count))
    