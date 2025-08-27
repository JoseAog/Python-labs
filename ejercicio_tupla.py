alumnos = {
    "Ana": [7, 9],
    "Luis": [8, 6],
    "Marta": [9, 10],
    "Carlos": [5, 7]
}
print("Claves del diccionario:", alumnos.keys())
for nombre in alumnos:
    mate = int(input(f"Introduce la nota de Matematicas de {nombre}: "))
    fisica = int(input(f"Introduce la nota de Fisica de {nombre}: "))
    alumnos[nombre] = [mate, fisica]
notas_mate = [notas[0] for notas in alumnos.values()]
print("Notas de matematicas:", notas_mate)
alumnos_top = {nombre for nombre, notas in alumnos.items() if any(n > 8 for n in notas)}
print("Alumnos con alguna nota > 8:", alumnos_top)
todas_notas = list(alumnos.values())
print("Todas las notas:", todas_notas)