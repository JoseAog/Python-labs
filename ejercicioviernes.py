while True:
    print("\n--- Calculadora ---")

    entrada1 = input("Escribe un numero (o 'salir' para terminar):")
    if entrada1.lower() == "salir":
        print("Saliendo de la calculadora hasta luego")
        break
    try:
        num1 = float(entrada1)
    except ValueError:
        print("Error: Por favor escribe un numero valido.")
        continue

    entrada2 = input("Escribe el siguiente numero (o 'salir' para terminar):")
    if entrada2.lower() == "salir":
        print("Saliendo de la calculadora hasta luego")
        break
    try:
        num2 = float(entrada2)
    except ValueError:
        print("Error. Por favor escribe un numero valid.")
        continue
    operacion = input("¿Que operacion quieres hcer? (suma,resta,multiplicacion,potencia,division o salir): ").lower()
    if operacion == "salir":
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicacion":
        resultado = num1 * num2
    elif operacion == "potencia":
        if num1 > 100 or num2 > 100:
            resultado = "Error: El exponente es demasiado grande". capitalize ()
        else:
            resultado = num1 ** num2
    elif operacion == "division":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: No se puede dividir entre cero"
    else:
        resultad = "Operacion no valida"
    print("Resultado:", resultado)
