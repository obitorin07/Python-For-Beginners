"""# Assignment: Python List Manipulation Practice


1. **Initialize an empty list called `numbers_list`.**
   - **Question:** How do you initialize an empty list in Python?

2. **Append the numbers 10, 20, and 30 to `numbers_list`.**
   - **Question:** What method do you use to add elements to the end of a list in Python?

3. **Extend `numbers_list` with [40, 50, 60].**
   - **Question:** How do you add multiple elements to the end of a list in Python?

4. **Insert the number 5 at index 0 in `numbers_list`.**
   - **Question:** How do you insert an element at a specific index in a list in Python?

5. **Remove the last element from `numbers_list`.**
   - **Question:** What method do you use to remove the last element from a list in Python?

6. **Remove the element at index 2 from `numbers_list`.**
   - **Question:** How do you remove an element at a specific index from a list in Python?

7. **Print the index of the number 30 in `numbers_list`.**
   - **Question:** How do you find the index of a specific value in a list in Python?

8. **Count the number of occurrences of the number 20 in `numbers_list`.**
   - **Question:** How do you count the number of occurrences of a specific value in a list in Python?

9. **Create a copy of `numbers_list` called `new_numbers_list`.**
   - **Question:** What method do you use to create a shallow copy of a list in Python?

10. **Sort `new_numbers_list` in ascending order.**
    - **Question:** How do you sort a list in ascending order in Python?

11. **Reverse `new_numbers_list`.**
    - **Question:** How do you reverse the order of elements in a list in Python?

12. **Create a list called `mixed_data_list` containing a mix of integers, strings, and boolean values.**
    - **Question:** Can a list contain elements of different data types in Python?

13. **Append the string "world" to `mixed_data_list`.**
    - **Question:** How do you add a string element to the end of a list in Python?

14. **Extend `mixed_data_list` with [True, False].**
    - **Question:** How do you add multiple elements to the end of a list in Python?

15. **Remove all occurrences of the number 20 from `mixed_data_list`.**
    - **Question:** How do you remove all occurrences of a specific value from a list in Python?

16. **Print the length of `mixed_data_list`.**
    - **Question:** How do you find the number of elements in a list in Python?

17. **Print the first and last elements of `mixed_data_list`.**
    - **Question:** How do you access the first and last elements of a list in Python?

18. **Check if the number 10 is in `mixed_data_list`.**
    - **Question:** How do you check if a value is present in a list in Python?

19. **Find the maximum and minimum values in `mixed_data_list`.**
    - **Question:** How do you find the maximum and minimum values in a list in Python?

20. **Create a sublist of `mixed_data_list` containing only integers.**
    - **Question:** How do you create a sublist of elements based on a condition in Python?

21. **Count the number of strings in `mixed_data_list`.**
    - **Question:** How do you count the number of elements satisfying a condition in a list in Python?

22. **Remove duplicates from `mixed_data_list`.**
    - **Question:** How do you remove duplicates from a list in Python?

23. **Replace all occurrences of the string "world" with "hello" in `mixed_data_list`.**
    - **Question:** How do you replace all occurrences of a value in a list in Python?

24. **Clear all elements from `mixed_data_list`.**
    - **Question:** How do you remove all elements from a list in Python?
"""


# Initialize an empty list called numbers_list.

# Question: How do you initialize an empty list in Python?

numbers_list =[]

# Append the numbers 10, 20, and 30 to numbers_list.
numbers_list.append(10)
numbers_list.append(20)
numbers_list.append(30)
print(numbers_list)

#Extend numbers_list with [40, 50, 60].
numbers_list.extend([40,50,60])
print("After Extending :",numbers_list)

#Insert the number 5 at index 0 in numbers_list.
numbers_list.insert(0,5)
print("After Inserting Value in 0th Index ",numbers_list)

#Remove the last element from numbers_list.
numbers_list.pop()
#numbers_list.pop(-1)
print("Remove Last Elment",numbers_list)

#Remove the element at index 2 from numbers_list.
numbers_list.pop(2)
print("Afer Remove data from 2nd index",numbers_list)

#Print the index of the number 30 in numbers_list.
display_index_position=numbers_list.index(30)
print("The Position of 30 is ",display_index_position)

#Count the number of occurrences of the number 20 in numbers_list.
counting =numbers_list.count(20)
print(counting)

#Create a copy of numbers_list called new_numbers_list.
new_numbers_list =numbers_list.copy()
print(new_numbers_list)

#Sort new_numbers_list in ascending order.
#they are already in asc order
new_numbers_list.sort()
print(new_numbers_list)

#Reverse new_numbers_list.
new_numbers_list.reverse()
print("Reverse Value :",new_numbers_list)

#Create a list called mixed_data_list containing a mix of integers, strings, and boolean values.
mixed_data_list= ["Hello iam Obitorin","20",True,"Anime","Python",True]
print(mixed_data_list)

#Append the string "world" to mixed_data_list.
mixed_data_list.append("world")
print("After Adding Value 'World' In existing list is:",mixed_data_list)

#Extend mixed_data_list with [True, False]
mixed_data_list.extend([True,False])
print(mixed_data_list)

#Remove all occurrences of the number 20 from mixed_data_list.
#there is no 20 in list but there one 20 but as a string lets remove that
mixed_data_list.remove("20")
print("After removing 20 from list",mixed_data_list)

#Print the length of mixed_data_list.
print("The Length of mixed_data_list",len(mixed_data_list))

#Print the first and last elements of mixed_data_list
print("The Starting Element is :",mixed_data_list[0])
print("The Last Element is :",mixed_data_list[-1])

#Check if the number 10 is in mixed_data_list
#so there is no 10 in our list 
if 10 in mixed_data_list:
    print("yes Exist" )
else:
    print("Not Exist")

#Find the maximum and minimum values in mixed_data_list
    #this will not support for bool and str 
# minimum =min(mixed_data_list)
# maximum =max(mixed_data_list)

# print("The Minimum Value :",minimum)
# print("The Maximum Value :",maximum)

#Create a sublist of mixed_data_list containing only integers.
new = [20,20,5,12,15]
mixed_data_list.append(new)
print(mixed_data_list)
#Count the number of strings in mixed_data_list.
string_count= sum( type(i)==str for i in mixed_data_list)
print("Number of String Exist in List :",string_count)

#Remove duplicates from mixed_data_list.
#lets create new empty list called clean_data_list

clean_data_list =[]
for unique in mixed_data_list:
    if unique not in clean_data_list:
        clean_data_list.append(unique)
print("Accurate Data Without Duplication:",clean_data_list)

#Clear all elements from mixed_data_list.
clean_data_list.clear()
print("_________________________________")
print("After Clean perform",clean_data_list)