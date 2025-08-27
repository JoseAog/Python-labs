def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor introduce un numero valido.")
def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "**":
        return num1 ** num2
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error. division por cero"
    else:
        return "Operacion no valida"
    
def main():
    while True:
        num1 = pedir_numero("Escribe el primer numero: ")
        num2 = pedir_numero("Escribe el segundo numero:")
        operacion = input ("¿Que operacion deseas realizar? (+,-,*,**,/): ").strip()
        resultado = calcular(num1, num2, operacion)
        print(f"Resultado:{resultado}")
        repetir = input("¿Deseas realizar otra operacion? (si,no): ").strip().lower()
        if repetir != "si":
            break
main()