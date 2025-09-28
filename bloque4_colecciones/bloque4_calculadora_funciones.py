def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    while True:
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
        except ValueError:
            print("Introduce un número válido.")
            continue

        operacion = input("Operación (+, -, *, /) o 'salir' para terminar: ").strip()
        if operacion == "salir":
            print("Saliendo de la calculadora...")
            break

        if operacion == "+":
            resultado = suma(num1, num2)
        elif operacion == "-":
            resultado = resta(num1, num2)
        elif operacion == "*":
            resultado = multiplicacion(num1, num2)
        elif operacion == "/":
            resultado = division(num1, num2)
        else:
            resultado = "Operación no válida"

        print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora()
