color = input("Introduce un color del semaforo (rojo,amarillo,verde): ")

if color == "rojo":
    print("alto")
elif color == "amarillo":
    print("precaucion")
elif color == "verde":
    print("sigue")
else:
    print("color no valido")