# Ejemplo de herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "Hace un sonido"

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

# Ejemplo de uso
if __name__ == "__main__":
    perro = Perro("Bobby")
    gato = Gato("Misu")
    print(f"{perro.nombre} dice: {perro.hablar()}")
    print(f"{gato.nombre} dice: {gato.hablar()}")
