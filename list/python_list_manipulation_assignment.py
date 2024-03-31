

"""Assignment: Python List Manipulation
 Create an empty list called my_list.
 Append the numbers 1, 2, and 3 to my_list.
 Append the string "hello" to my_list.
 Print the length of my_list.
 Print the first element of my_list.
 Print the last element of my_list.
 Insert the number 10 at index 1 in my_list.
 Remove the string "hello" from my_list.
 Remove the element at index 2 from my_list.
 Print the index of the number 3 in my_list.
 Count the number of occurrences of the number 2 in my_list.
 Create a copy of my_list called new_list.
 Extend new_list with [4, 5, 6].
 Sort new_list in ascending order.
 Reve rse new_list. erse new_list."""



my_list =[]

#this also valid 
# list_add =[1,2,3]
# add =my_list.extend(list_add)
#print(my_list)

my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)

#adding string in existing list
greeting ="Hello"
my_list.append(greeting)
print(my_list)

#checking the length of the list
print(len(my_list))

#print the first element from the list
print(my_list[0])


#print the last element from the list
print(my_list[-1])

# Insert the number 10 at index 1 in my_list
my_list.insert(1,10)
print(my_list)

# Remove the string "hello" from my_list.
my_list.remove("Hello")
print(my_list)

#Remove the element at index 2 from my_list
my_list.pop(2)
print(my_list)

#Print the index of the number 3 in my_list

#this will definitely show an error because there are only  3 elements are left with 2 index 

#print(my_list[3
print(my_list[-1])

#Count the number of occurrences of the number 2 in my_list.
#currently we dont have anything it willl display 0
print(my_list.count(2))

#Create a copy of my_list called new_list.
new_list = my_list.copy()
print("The new list",new_list)

#Extend new_list with [4, 5, 6].
new_list.extend([4,5,6])
print("After Extend 4,5,6:",new_list)

# Sort new_list in ascending order.
new_list.sort()
print(new_list)

#Reverse new_list.
new_list.reverse()
print(new_list)