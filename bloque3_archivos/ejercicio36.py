import csv
with open("estudiantes.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    encabezados = next(lector)
    estudiantes = []
    for fila in lector:
        nombre = fila[0]
        edad = int(fila[1])
        nota = float(fila[2])
        estudiantes.append((nombre, edad, nota))
promedio = sum(nota for _, _, nota in estudiantes) / len(estudiantes)
print(f"Promedio general de notas: {promedio:.2f}")
print("\nEstudiantes aprobados:")
for nombre, edad, nota in estudiantes:
    if nota >= 5:
        print(f"- {nombre} ({edad} años) con nota {nota}")