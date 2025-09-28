# Proyecto POO: Gestión de Estudiantes
class Estudiante:
    def __init__(self, nombre, edad, notas=None):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas if notas else []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - Promedio: {self.promedio():.2f}"

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"Curso: {self.nombre}")
        for est in self.estudiantes:
            print(est)

# Ejemplo de uso
if __name__ == "__main__":
    curso = Curso("Python")
    e1 = Estudiante("Lucía", 20, [8, 9, 7])
    e2 = Estudiante("Juan", 22, [6, 5, 7])
    curso.agregar_estudiante(e1)
    curso.agregar_estudiante(e2)
    curso.mostrar_estudiantes()
