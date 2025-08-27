import random
def jugar():
    numero_secreto = random.randint(1, 10)
    intentos = 0
    historial = []
    print("Adivina el numero (entre 1 y 10)")
    while True:
        try:
            intento = int(input("Introduce tu numero: "))
            intentos += 1
            historial.append(intento)
            if intento == numero_secreto:
                print(f"Acertaste en {intentos} intentos")
                break
            elif intento < numero_secreto:
                print("El numero secreto es mas grande.")
            else:
                print("El numero secreto es mas pequeño.")
        except ValueError:
            print("Solo puedes escribir numeros enteros.")
    with open("historial_juego.txt", "a") as f:
        f.write(f"Intentos: {historial} -> Ganado en {intentos} intentos\n ")
        print("Historial guardado en 'historial_juego.txt'")
jugar()