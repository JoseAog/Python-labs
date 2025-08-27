while True:
    num1 = float(input("Escribe un numero: "))
    num2 = float(input("Escribe el segundo numero:"))
    operacion = input("¿Que operacion deseas realizar?, (+,-,*,/): ")
    if operacion == "+":
        resultado = num1 + num2
        print("El resultado es:", resultado)
    elif operacion == "-":
        resultado = num1 - num2
        print("El resultado es:", resultado)
    elif operacion == "*":
        resultado = num1 * num2
        print("El resultado es:", resultado)
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado es:", resultado)
        else:
            print("error. no se puede dividir entre 0")
    else:
        print("operacion no valida")
    repetir = input("¿Deseas repetir?, (si,no):").strip().lower()
    if repetir == "no":
        break