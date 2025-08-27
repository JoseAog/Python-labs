num_alumnos = int(input("¿Cuantos alumnos deseas registrar?: "))
alumnos = {}
for i in range(num_alumnos):
    nombre = input(f"\nNombre del alumno {i+1}: ")
    notas = {
        "Matematicas": [],
        "Lengua": [],
        "Ciencias": []
    }
    for materia in notas.keys():
        for j in range(3):
            nota = float(input(f"Introduce nota {j+1} de {materia} para {nombre}: "))
            notas[materia].append(nota)
        alumnos[nombre] = notas
print("\n===== RESULTADOS =====")
aprobados = set()
suspensos = set()
for alumno, materias in alumnos.items():
    todas_notas = []
    for materia, lista_notas in materias.items():
        promedio_materia = sum(lista_notas) / len(lista_notas)
        print(f"{alumno} - {materia}: {promedio_materia:.2f}")
        todas_notas.extend(lista_notas)
    promedio_total = sum(todas_notas) / len(todas_notas)
    print(f"Promedio general de {alumno}: {promedio_total:.2f}\n")
    if promedio_total >= 5:
        aprobados.add(alumno)
    else:
        suspensos.add(alumno)
print("Alumnos aprobados:", aprobados)
print("Alumnos suspensos:", suspensos)
print("Todos los alumnos registrados:", set(alumnos.keys()))