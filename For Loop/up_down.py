#!/usr/bin/env python3
#day unknown i dont remembered i didnt count day i just do practice everyday thats all

"""Question👇

Ask which direction the user wants to count (up or down). If they select up, then ask 
them for the top number and then count from 1 to that number. If they select down, ask 
them to enter a number below 20 and then count down from 20 to that number. If they 
entered something other than up or down, display the message “I don’t understand”. """

up_down =input ("Which direction you want to count ? (Up/Down):").lower()

if up_down=='up':
	top_number = int(input("Enter The Top Number :"))
	for i in range(1,top_number+1,1): 
	#for i in range(1,top_number+1) default it step1 #(start,stop,step)
		print(i)
elif up_down =='down':
	down_number =int(input("Enter The Below 20 Number :"))

	#i use extra conditon because 
	if down_number <=20:
		for i in range(20,down_number-1,-1):
			print(i)
	else:
		print("Please Enter Number Below 20")
else:
	print("I dont understand🙄")