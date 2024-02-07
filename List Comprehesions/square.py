#!/usr/bin/env python3
# it prints sqaure numbers from 0 to 10
x = int(input("Enter Range:"))
result =[i**2 for i in range(0,x+1)]
#print(result.append(empty_list))
print(result)


""""Output
Enter Range:10
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""