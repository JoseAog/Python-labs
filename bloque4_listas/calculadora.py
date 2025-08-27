operaciones = {
    "sumar": lambda x, y: x + y,
    "restar": lambda x, y: x - y,
    "multiplicar": lambda x, y: x * y,
    "dividir": lambda x, y: x / y if y != 0 else "Error: division entre cero"
}
x = float(input("Introduce el primer numero: "))
y = float(input("Introduce el segundo numero: "))
print("Tipo de x:", type(x))
print("Tipo de y:", type(y))
operacion = input("¿Que operacion deseas realizar? (sumar, restar, multiplicar, dividir): ")
match operacion:
    case "sumar" | "restar" | "multiplicar" | "dividir":
        resultado = operaciones[operacion] (x,y)
        print(f"El resultado de {operacion} {x} y {y} es: {resultado} ")
    case _:
        print("Operacion no valida.")