# Ejemplo de uso de tuplas
tupla_colores = ("rojo", "verde", "azul")
print("Tupla completa:", tupla_colores)

# Acceso a elementos
print("Primer color:", tupla_colores[0])

# Iterar
print("Colores disponibles:")
for color in tupla_colores:
    print("-", color)

# Convertir a lista para modificar
lista_colores = list(tupla_colores)
lista_colores.append("amarillo")
tupla_colores = tuple(lista_colores)
print("Tupla modificada:", tupla_colores)
