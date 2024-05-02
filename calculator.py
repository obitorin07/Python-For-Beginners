#!/usr/bin/env python3
#this is shebang or hashbang



class calculator:
    #constructor
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.choice= ""
        self.menu()

    def add(self):
        result = self.num1+self.num2
        return "The Addition Of {} and {} is {}".format(self.num1,self.num2,result)

    def subtract(self):
        result = self.num1 - self.num2
        return "The Subtraction Of {} from {} is {}".format(self.num2, self.num1, result)

    def multiply(self):
        result = self.num1 * self.num2
        return "The Multiplication Of {} and {} is {}".format(self.num1, self.num2, result)

    def divide(self):
        if self.num2 != 0:
            result = self.num1 / self.num2
            return "The Division Of {} by {} is {}".format(self.num1, self.num2, result)
        else:
            return "Cannot divide by zero."
    def menu(self):
        print(""""Calculator
        1.Addition
        2.Subtraction
        3.Multiplication
        4.Division""")

        self.choice = input("Enter Numbers between 1-4:")

        if self.choice=="1":
            print(self.add())
        elif self.choice =="2":
            print(self.subtract())
        elif self.choice=="3":
           print( self.multiply())
        elif self.choice =="4":
            print(self.divide())
        else:
            exit()


first_number = float(input("Enter The First Number:"))
#it will ask user first number

second_number = float(input("Enter The Second Number:"))
#it will ask user enter second number


obj = calculator(first_number,second_number)
obj.menu()
obj.add()
obj.subtract()
obj.multiply()
obj.divide()