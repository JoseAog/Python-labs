print("Calculadora simple")

try:
    # Entradas
    num1 = float(input("Escribe el primer numero: "))
    num2 = float(input("Escribe el segundo numero: "))

    # Operaciones
    print("\nResultados:")
    print("Suma:", num1 + num2)
    print("Resta:", num1 - num2)
    print("Multiplicacion:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
        print("Division entera:", num1 // num2)
        print("Modulo:", num1 % num2)
    else:
        print("no se puede dividir entre cero.")

    print("Potencia:", num1 ** num2)
except ValueError:
    print("X Error: Solo puedes escribir numeros, no letras ni simbolos.")

except Exception as e:
        print(f" X Has ocurrido un error inesperado: {e}")