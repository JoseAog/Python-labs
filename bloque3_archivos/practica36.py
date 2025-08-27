import csv
import random
archivo = "estudiantes.csv"
with open(archivo, "r", newline="") as fr:
    lector = csv.reader(fr)
    next(lector, None)
    print("Lista de estudiantes: ")
    for fila in lector:
        print(fila)

nombre = input("Introduce el nombre del estudiante: ")
edad = input("Introduce la edad: ")
nota = input("Introduce la nota: ")
estudiante_id = random.randint(1000, 9999)

with open(archivo, "a", newline="") as fw:
    escritor = csv.writer(fw)
    escritor.writerow([estudiante_id, nombre, edad, nota])
    print("Estudiante añadido corrrectamente. ")