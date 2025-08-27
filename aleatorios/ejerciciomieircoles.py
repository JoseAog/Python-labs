num1 = int(input("Escribe un numero:"))
num2 = int(input("Escribe el segundo numero:"))
operacion = input("¿Que operacion quieres realizar?, (suma, resta, multiplicacion, division):" )

if operacion == "suma":
    print("resultado:", num1 + num2)
elif operacion == "resta":
    print("resultado:", num1 - num2)
elif operacion == "multiplicacion":
    print("resultado:", num1 * num2)
elif operacion == "division":
    if num2 == 0:
        print("resultado:", ("error no se puede dividir entre cero"))
    else:
        print("resultado:", num1 / num2)
else:
    print("resultado:", ("Error: operacion no disponible"))
