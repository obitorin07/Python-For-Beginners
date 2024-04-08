#we just change simple mode only "w " to "a"

import csv

name =input("Enter The Name :").capitalize()
age =int(input("Enter The Age :"))
place =input("Enter The Place :").capitalize()

with open ("Obito_rin.csv","a",newline="") as file:
    csv_writter=csv.writer(file)

    csv_writter.writerow([name,age,place])
