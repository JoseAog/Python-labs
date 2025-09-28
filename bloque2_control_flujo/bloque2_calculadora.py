# Calculadora interactiva completa
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número válido.")

def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: división por cero"
    else:
        return "Operación no válida"

def main():
    print("--- Calculadora ---")
    while True:
        num1 = pedir_numero("Escribe el primer número: ")
        num2 = pedir_numero("Escribe el segundo número: ")
        operacion = input("Elige operación (+, -, *, /): ").strip()
        resultado = calcular(num1, num2, operacion)
        print(f"Resultado: {resultado}")
        if input("¿Deseas realizar otra operación? (si/no): ").strip().lower() != "si":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
