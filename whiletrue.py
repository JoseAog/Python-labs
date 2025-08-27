while True:
    print("\nMenú:")
    print("1. Saludar")
    print("2. Sumar dos numeros")
    print("3. Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        nombre = input("¿Como te llamas? ")
        print("¡Hola,", nombre, "!")
    elif opcion == "2":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero:"))
        print("Resultado:", num1 + num2)
    elif opcion == "3":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida. Intentalo de nuevo")