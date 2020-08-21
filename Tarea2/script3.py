import csv
print("/\/\/\/\/\/\/\/ CSV \/\/\/\/\//\/\/")
with open('doc3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print("\n","Nombre: {0}\n Apellido: {1}\n Edad: {2}\n Estudia: {3}\n tipo: ".format(row[0], row[1], row[2], row[3]),type(row))

