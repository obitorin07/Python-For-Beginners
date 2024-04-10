people =["A","B","C","D","E","F","G","H","I"]
with open ("add_people.txt","w") as file:
    for i in people:
        file.write(f"{i}\n")
