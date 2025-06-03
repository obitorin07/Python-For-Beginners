"""

🧠 Problem 3: Delivery Filter – Only Deliver to Nearby Areas
You’re running a food delivery service.
These are the areas where you got orders:

Using list comprehension, create a new list valid_orders that only keeps orders from allowed zones.
Count how many orders were valid.

Print the updated list and count.

(Optional twist): Remove duplicates from the valid_orders list (just for cleanup).
"""

orders = ["Wakad", "Baner", "Kothrud", "Hadapsar", "Wakad", "Viman Nagar", "Baner"]
allowed_zones = ["Wakad", "Baner", "Kothrud"]

valid_orders =  [order for order in orders if order in allowed_zones]
print(valid_orders)
print("Number of orders are valid",len(valid_orders))
print(set(valid_orders))

emp_list = []
for i in valid_orders:
    if i not in emp_list:
        emp_list.append(i)
    else:
        continue
print(emp_list)