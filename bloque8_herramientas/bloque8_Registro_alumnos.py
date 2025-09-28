alumnos = {}

print("=== Registro de Alumnos ===")

# Cargar desde archivo
try:
    with open("alumnos.txt", "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            nombre = datos[0]
            notas = list(map(float, datos[1:]))
            alumnos[nombre] = notas
except FileNotFoundError:
    print("Archivo no encontrado, se creará uno nuevo al guardar.")

# Mostrar alumnos existentes
if alumnos:
    print("\nAlumnos actuales:")
    for nombre, notas in alumnos.items():
        print(f"{nombre}: {notas}")

# Función promedio
def promedio(notas):
    return sum(notas) / len(notas)

# Mostrar resultados
for nombre, notas in alumnos.items():
    media = promedio(notas)
    estado = "Aprobado" if media >= 5 else "Suspenso"
    print(f"{nombre}: {media:.2f} ({estado})")

# Nuevo alumno
nuevo_nombre = input("\nIntroduce el nombre del nuevo estudiante: ")
nuevas_notas = [float(input(f"Introduce la nota {i+1}: ")) for i in range(3)]
alumnos[nuevo_nombre] = nuevas_notas

# Guardar archivo actualizado
with open("alumnos.txt", "w") as f:
    for nombre, notas in alumnos.items():
        linea = nombre + "," + ",".join(map(str, notas)) + "\n"
        f.write(linea)

print("\nArchivo actualizado con todos los estudiantes.")
