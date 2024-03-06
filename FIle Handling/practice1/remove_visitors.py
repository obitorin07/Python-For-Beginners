#!/usr/bin/env python3

remove_visitors =['naruto','hinata','sakura','sasuke']
temp =[]
with open ('remove_visitors.txt')as rm:
	for i in rm:
		temp.append(i)

with open('remove_visitors.txt','w')as rm:
	for i in temp:
		if i.strip() not in remove_visitors:
			rm.write(f' {i.strip()}\n')
