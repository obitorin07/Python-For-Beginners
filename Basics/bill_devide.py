#!/usr/bin/env python3
#challenge 7
"""Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay."""

total_price =int(input("Enter Total Price Of Bill:"))
how_many_diners=int(input("Enter How Many Diners:"))
each_pay =total_price/how_many_diners

print("Each Person Need Pay $",each_pay)