while True:
    num1 = float(input("Escribe un numero: "))
    num2 = float(input("Escribe un segundo numero: "))
    operacion = input("¿Que operacion deseas realizar? (suma, resta, multiplicacion, division):")
    
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicacion":
        resultado = num1 * num2
    elif operacion == "division":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error. No se puede dividir entre cero"
    else:
        resultado = "operacion no valida"
    print("El resultado es:", resultado)
    repetir = input("¿Deseas hacer otra operacion? (si/no): ")
    if repetir == "no":
        break