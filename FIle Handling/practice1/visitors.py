#!/usr/bin/env python3
# scinario we have visitors in hotel


# we create text file name called visitors.txt

visitors = open("visitors.txt","w")

visitors_name = ['obito','rin','naruto','hinata','sakura','sasuke']

for i in visitors_name:
	visitors.write(i +'\n')

visitors.close()