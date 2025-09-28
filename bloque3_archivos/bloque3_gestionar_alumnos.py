# Gestión de alumnos con archivos
def cargar_alumnos(archivo="alumnos.txt"):
    alumnos = {}
    try:
        with open(archivo, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                nombre = datos[0]
                notas = list(map(float, datos[1:]))
                alumnos[nombre] = notas
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo al guardar.")
    return alumnos

def guardar_alumnos(alumnos, archivo="alumnos.txt"):
    with open(archivo, "w") as f:
        for nombre, notas in alumnos.items():
            f.write(nombre + "," + ",".join(map(str, notas)) + "\n")
    print("Archivo actualizado con todos los estudiantes.")

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def mostrar_alumnos(alumnos):
    print("\n=== ESTUDIANTES ACTUALES ===")
    for nombre, notas in alumnos.items():
        promedio = calcular_promedio(notas)
        estado = "aprobado" if promedio >= 5 else "suspendido"
        print(f"{nombre}: {notas} -> {estado} ({promedio:.2f})")

def agregar_alumno(alumnos):
    nombre = input("\nIntroduce el nombre del nuevo estudiante: ")
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Introduce la nota {i}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Introduce un número válido.")
    alumnos[nombre] = notas
    promedio = calcular_promedio(notas)
    estado = "aprobado" if promedio >= 5 else "suspendido"
    print(f"{nombre} ha {estado} con promedio {promedio:.2f}")

def main():
    alumnos = cargar_alumnos()
    mostrar_alumnos(alumnos)
    agregar_alumno(alumnos)
    guardar_alumnos(alumnos)

if __name__ == "__main__":
    main()
