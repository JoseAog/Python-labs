# Clase básica
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Ejemplo de uso
if __name__ == "__main__":
    p1 = Persona("Ana", 25)
    print(p1.presentarse())
