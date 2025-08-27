alumnos = {}
try:
    with open("alumnos.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            nombre = datos[0]
            notas = list(map(float, datos[1:]))
            alumnos[nombre] = notas
except FileNotFoundError:
    print("Archivo no encontrado.")
print("\nEstudiantes actuales: ")
for nombre, notas in alumnos.items():
    print(f"{nombre}: {notas}")
def promedio(notas):
    return sum(notas) / len(notas)
for nombre, notas in alumnos.items():
    media = promedio(notas)
    estado = "aprobado" if media >= 5 else "suspendido"
    print(f"{nombre} ha {estado} con promedio {media:.2f}")
nuevo_nombre = input("Introduce el nombre del nuevo estudiante: ")
nueva_notas = []
for i in range(1, 4):
    nota = float(input(f"Introduce la nota {i}: "))
    nueva_notas.append(nota)
alumnos[nuevo_nombre] = nueva_notas
with open("alumnos.txt", "w") as f:
    for nombre, notas in alumnos.items():
        linea = nombre + "," + ",".join(map(str,notas)) + "\n"
        f.write(linea)
print("\nArchivo actualizado con todos los estudiantes.")