#!/usr/bin/env python3
# """ Can you write a Python function that takes a list of numbers as input and returns the sum of all the numbers in the list? """
#
#solving method 1
# def sum_list(number):
#     result =sum(number)
#     return f'The Sum of {number} is {result}'
# number=[1,2,3,4,5,6,7]
# print(sum_list(number))


#solving method2

def sum_list(number):
    add = 0
    for i in number:
        add =i+add
    return f'the sum {number} is {add}'

number = [1, 2, 3, 4, 5, 6, 7]
print(sum_list(number))