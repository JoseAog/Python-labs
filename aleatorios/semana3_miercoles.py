def calcular_promedio(notas):
    return sum(notas) / len(notas)
estudiantes = {
    "Ana": [7, 8, 6],
    "Luis": [4, 5, 5],
    "Maria": [9, 8, 10]
}
nuevo_nombre = input("Nombre del nuevo estudiante: ")
nuevas_notas = []
for i in range(3):
    nota = float(input(f"Introduce la nota {i + 1} de {nuevo_nombre}: "))
    nuevas_notas.append(nota)
estudiantes[nuevo_nombre] = nuevas_notas
for nombre, notas in estudiantes.items():
    promedio = calcular_promedio(notas)
    if promedio >= 5:
        print(f"{nombre} ha aprobado con una media de {promedio:.2f}")
    else:
        print(f"{nombre} ha suspendido con una media de {promedio:.2f}")