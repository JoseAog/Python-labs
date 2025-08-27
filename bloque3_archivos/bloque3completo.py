import csv
import random
import statistics
def agregar_estudiante_txt(nombre, edad, nota, archivo="estudiantes.txt"):
    try:
        with open(archivo, "a") as f:
            f.write(f"{nombre}, {edad}, {nota}\n")
    except Exception as e:
        print(f"Error al escribir en el archivo TXT: {e}")
def leer_estudiantes_txt(archivo="estudiates.txt"):
    estudiantes = []
    try:
        with open(archivo, "r") as f:
            for linea in f:
                nombre, edad, nota = linea.strip().split(",")
                estudiantes.append({
                    "nombre": nombre,
                    "edad": int(edad),
                    "nota": float(nota)
                })
    except FileNotFoundError:
        print("Archivo TXT no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo TXT: {e}")
    return estudiantes
def guardar_csv(estudiantes, archivo="estudiantes.csv"):
    try:
        with open(archivo, "w", newline="") as csvfile:
            campos = ["nombre", "edad", "nota"]
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            for est in estudiantes:
                writer.writerow(est)
    except Exception as e:
        print(f"Error al guardar CSV: {e}")
def leer_csv(archivo="estudiantes.csv"):
    estudiantes = []
    try:
        with open(archivo, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                estudiantes.append({
                    "nombre": row["nombre"],
                    "edad": int(row["edad"]),
                    "nota": float(row["nota"])
                })
    except FileNotFoundError:
        print("Archivo CSV no encontrado.")
    except Exception as e:
        print(f"Error al leer CSV: {e}")
    return estudiantes
def generar_estudiantes_aleatorios(n=10):
    nombres = ["Ana","Luis", "Marta", "Carlos", "Lucia", "Javier", "Sofia", "Diego", "Elena", "Mario"]
    estudiantes = []
    for _ in range(n):
        nombre = random.choice(nombres)
        edad = random.randint(18, 25)
        nota = round(random.uniform(5, 10), 2)
        estudiantes.append({"nombre": nombre, "edad": edad, "nota": nota})
    return estudiantes
def menu():
    estudiantes = leer_csv()
    while True:
        print("\nOpciones:")
        print("1. Mostrar estudiantes")
        print("2. Agregar estudiante")
        print("3. Eliminar estudiante")
        print("4. Modificar estudiante")
        print("5. Generar TXT y CSV final")
        print("6. Estadisticas de notas")
        print("0. Salir")
        opcion = input("Selecciona opción:")
        if opcion == "1":
            for est in estudiantes:
                print(est)
        elif opcion == "2":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            nota = float(input("Nota: "))
            estudiantes.append({"nombre": nombre, "edad": edad, "nota": nota})
        elif opcion == "3":
            nombre = input("Nombre a eliminar: ")
            estudiantes = [e for e in estudiantes if e["nombre"] != nombre]
        elif opcion == "4":
            nombre = input("Nombre a modificar: ")
            encontrado = False
            for est in estudiantes:
                if est["nombre"] == nombre:
                    est["edad"] = int(input("Nueva edad: "))
                    est["nota"] = float(input("Nueva nota:"))
                    encontrado = True
            if not encontrado:
                print("Estudiante no encontrado.")
        elif opcion == "5":
            guardar_csv(estudiantes)
            for est in estudiantes:
                agregar_estudiante_txt(est["nombre"], est["edad"], est["nota"])
                print("Archivos generados correctamente.")
        elif opcion == "6":
            notas = [e["nota"] for e in estudiantes]
            if notas:
                print(f"Media: {statistics.mean(notas):.2f}")
                print(f"Mediana: {statistics.median(notas):.2f}")
                print(f"Desviacion estandar: {statistics.stdev(notas):.2f}")
            else:
                print("No hay notas para calcular estadisticas.")
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")
if __name__ == "__main__":
    estudiantes_aleatorios = generar_estudiantes_aleatorios()
    guardar_csv(estudiantes_aleatorios)
    menu()