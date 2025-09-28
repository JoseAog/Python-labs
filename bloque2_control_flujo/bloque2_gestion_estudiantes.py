# Gestión de estudiantes con promedios
def pedir_nota(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Introduce un número válido.")

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def main():
    alumnos = {}
    
    # Ingreso de alumnos existentes
    num_alumnos = int(input("¿Cuántos alumnos deseas registrar?: "))
    for i in range(num_alumnos):
        nombre = input(f"\nNombre del alumno {i+1}: ")
        notas = []
        for j in range(1, 4):
            notas.append(pedir_nota(f"Introduce nota {j}: "))
        alumnos[nombre] = notas
    
    print("\n=== RESULTADOS ===")
    for nombre, notas in alumnos.items():
        promedio = calcular_promedio(notas)
        estado = "aprobado" if promedio >= 5 else "suspendido"
        print(f"{nombre} ha {estado} con promedio {promedio:.2f}")

if __name__ == "__main__":
    main()
