print("=== Promedio de Estudiantes ===")

try:
    n = int(input("¿Cuántos estudiantes quieres registrar? "))
    if n <= 0:
        print("El número debe ser mayor que 0.")
        exit()

    estudiantes = {}
    for i in range(n):
        nombre = input(f"\nNombre del estudiante {i+1}: ")
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"  Nota {j+1}: "))
                    notas.append(nota)
                    break
                except ValueError:
                    print("Introduce un número válido.")
        promedio = sum(notas) / len(notas)
        estudiantes[nombre] = promedio

    print("\nResultados:")
    for nombre, promedio in estudiantes.items():
        estado = "Aprobado" if promedio >= 5 else "Suspenso"
        print(f"{nombre}: {promedio:.2f} ({estado})")

except ValueError:
    print("Entrada inválida.")
