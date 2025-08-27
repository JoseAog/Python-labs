num1 = input("Introduce el primer numero:")
num2 = input("Introduce el segundo numero:")
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Error: Debes introducir un numero valido.")
    exit()
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
try:
    division = num1 / num2
except ZeroDivisionError:
    division = "No se puede dividir por cero"
print("\nResultados:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)