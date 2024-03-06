#!/usr/bin/env python3
new =['Kakashi','Might Guy','Minato']
with open ("visitors.txt","a") as new_visitor:
	
	for i in new:
		new_visitor.write(f"Welcome New visitors {i}\n")
