"""
Problem 1: Analyzing Sales Data
The Scenario:
Imagine you work for a small e-commerce company. You've been given a list containing the dollar amounts of all individual sales made today. For a daily report, your manager wants to know the total revenue generated from sales that were an even dollar amount (e.g., $10, $52, $128). This kind of specific data slicing is common for tracking promotions or sales patterns.

Your Task:
Write a Python function called sum_of_even_sales that takes a list of numbers (representing sales) as an argument. The function should calculate and return the total sum of only the sales that are even numbers.

Example:

If the list of sales is ``.

The even-numbered sales are 10, 20, and 30.

Your function should return 60 (because 10 + 20 + 30 = 60).

Concepts This Will Test:

Defining and calling a function.

Looping through a list.

Using a conditional (if) statement to check for even numbers.

Adding values to a running total.



"""

def sum_of_even_sales(sales_value):
    even_total = 0
    for val in sales_value:
        if val % 2==0:
            even_total+=val
    return even_total
sales_amount = [1,20,52,35,20,50,60]
print(sum_of_even_sales(sales_amount))