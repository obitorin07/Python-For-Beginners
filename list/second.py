"""
🧠 Problem 2: Student Name Updater
You manage student attendance manually.

Change "Sneha" to "Snehalata"

Remove "Ajay" from the list

Insert "Priya" at position 2

Append "Ravi" at the end

Print the updated student list
"""
students = ["Kiran", "Sneha", "Rahul", "Neha", "Ajay"]

user_update = "Sneha"
remove_user = 'Ajay'
arr = len(students)
if user_update.strip().title() in students :
    for name in range(arr) :
        if students[name] == user_update.strip().capitalize():
            students[name] = "Snehalata"
            break
        else :
            continue
print(students)

# i can use just pop to remove but sometime we dont know the position
if remove_user.strip().title() in students :
    for i in range(arr):
        if students[i] == remove_user.strip().capitalize():
            students.pop(i)
            break
        else:
            continue
print(students)


students.insert(1,"Priya")
print(students)

students.append("Ravi")
print(students)