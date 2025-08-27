with open("diario.txt", "w") as f:
    f.write("Primer dia\n")
nueva_linea = input("Escribe algo que quieras añadir al diario: ")
with open("diario.txt", "a") as f:
    f.write(nueva_linea + "\n")
with open("diario.txt", "r") as f:
    contenido = f.read()
    print("\nContenido completo del diario:")
    print(contenido)