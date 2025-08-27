import math
import random
def pedir_datos():
    nombre = input("Ingresa tu nombre:").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacio")
    try:
        edad = int(input("Ingresa tu edad en años: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
    except ValueError as e:
        raise ValueError("Edad invalida, ingresa un numero entrero positivo") from e
    return nombre, edad
def calcular_edad(edad):
    meses = round(edad* 12)
    dias = round(edad * 365.25)
    return meses, dias
def main():
    try:
        nombre, edad = pedir_datos()
        meses, dias = calcular_edad(edad)
        puntuacion = random.randint(1, 100)
        resumen = {
            "Nombre": nombre,
            "Edad años": edad,
            "Edad meses": meses,
            "Edad dias": dias,
            "Puntuacion de prueba": puntuacion
        }
        print("\n--- Resumen ---")
        for k, v in resumen.items():
            print(f"{k}: {v}")
    except ValueError as e:
        print("Error:", e)
if __name__ == "__main__":
    main()        