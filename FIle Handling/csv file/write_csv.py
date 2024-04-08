import csv
data =[["NAME","AGE","PLACE"],["OBITO",25,"KONAHA"],["RIN",24,"JAPAN"]]
with open ("Obito_rin.csv","w",newline="") as file:
    csv_reader =csv.writer(file)
    for i in data:
        csv_reader.writerow(i)
