"""
✅ LEVEL 0 – LIST FUNDAMENTALS
🧠 Problem 1: Product List Checker
You run a small Kirana store.
Your tasks:
Print the first and last item.

Print how many items are in the list.

Check if "butter" is in the list.

Check if "salt" is in the list


Add "salt" to the list and print the updated list.
"""

products = ["bread", "milk", "eggs", "butter", "rice"]

print(f"First Item :{products[0]} and last Item is : {products[-1]}")

print("The Number of items in store", len(products))

if "butter" in products :
    print("yes butter available")
else:
    print("sorry bro we dont have")

user = "salt"
if user.strip().lower() in products :
    print(f"{user} is available do u want ?")
else :
    print(f"{user} not available")