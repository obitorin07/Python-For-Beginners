temp =[]
remove_people =input("Enter The Person You Want To Remove :").upper()
with open ("add_people.txt","r") as file:
    for i in file :
         temp.append(i.strip())

print(temp)
def remove_p(remove_people):
    return temp.remove(remove_people)

if remove_people in temp:
    print("YES AVAILABLE ")
    remove_p(remove_people)
    print(f"Removed Element :{remove_people}")
    print("New Temp",temp)

else:
    print("NOT AVAILABLE")

with open ("removed_people.py","w") as file:
    for i in temp :
        file.write(f"New People :{i}\n")


