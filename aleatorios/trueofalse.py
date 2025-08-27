with open("alumnos.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(",")
        print(datos)