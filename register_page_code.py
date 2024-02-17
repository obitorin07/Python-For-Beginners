#!/usr/bin/env python3
#this code i try to write in different way without our aplication going to terminate
#i made lot of mistakes 😜😜
first_name = ""
last_name = ""
user_age = ""
user_pass = ""


while True:
    first_name = input("Enter Your First Name: ").capitalize()
    if first_name.isalpha():
        print("Your First Name: ", first_name)
        break
    else:
        print("Error: Entered First Name is not alphabetic. Please try again.")

while True:
    last_name = input("Enter Your Last Name: ").capitalize()
    if last_name.isalpha():
        print("Your Last Name: ", last_name)
        break
    else:
        print("Error: Entered Last Name is not alphabetic. Please try again.")

while True:
    user_age = input("Enter Your Age: ")
    if user_age.isdigit():
        print("Your Age: ", user_age)
        break
    else:
        print("Error: Entered Age is not numeric. Please enter a valid numeric value.")

while True:
    user_pass = input("Enter The Password: ")
    user_confirm_pass = input("Confirm Password: ")
    if user_pass == user_confirm_pass:
        print("Password is set successfully.")
        break
    else:
        print("Error: Entered passwords do not match. Please try again.")

while True:
    number =int(input("Enter Your Mobile Number:"))
    if 10 ** 9 <= number < 10 ** 10:
        user_number ="+91"+ str(number)
        print("Your Mobile Number is ",user_number)
        break
    else:
        print("Entered Number is Not Valid:")
full_name =first_name+last_name
# Display all information
print("\nUser Information:")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", user_age)
print("Password:", user_pass)
print(f"{full_name} Your Number :{user_number}")


"""Output Demo"""
# User Information:
# First Name: Obito
# Last Name: Uchiha
# Age: 15
# Password: 123456
# ObitoUchiha Your Number :+919876543210