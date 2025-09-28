# Calculadora modular (nivel básico)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: división entre 0"

# Entrada de usuario
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("Error: ingresa un número válido.")
    exit()

# Resultados
print("Suma:", suma(num1, num2))
print("Resta:", resta(num1, num2))
print("Multiplicación:", multiplicacion(num1, num2))
print("División:", division(num1, num2))
