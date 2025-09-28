print("=== Operaciones con manejo de excepciones ===")

try:
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print("\nResultados:")
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    print("División:", a / b if b != 0 else "Error: división entre 0")

except ValueError:
    print("Error: debes introducir números válidos.")
