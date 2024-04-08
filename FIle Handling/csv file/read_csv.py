import csv
with open("Obito_rin.csv",newline="")as file:
    csv_reader =csv.reader(file)
    #next is used to skip header data or first row
    next(csv_reader)
    for data in csv_reader:
        NAME ,AGE,PLACE =data

        print("Name:{} Age :{} Place :{}".format(NAME,AGE,PLACE) )


