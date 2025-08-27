frutas_A = {"manzana", "pera", "platano", "kiwi"}
frutas_B = {"kiwi", "naranja", "pera", "sandia"}
print("Frutas A:", frutas_A)
print("Frutas B:", frutas_B)
print("Union:", frutas_A | frutas_B)
print("Interseccion:", frutas_A & frutas_B)
print("Solo en A:", frutas_A - frutas_B)
print("Exclusivos de A y B:", frutas_A ^ frutas_B)
print("¿Está 'manzana' en frutas_A?", "manzana" in frutas_A)
print("¿Está 'coco' en frutas_B?", "coco" in frutas_B)
estudiantes = {
    "Ana": 20,
    "Luis": 22,
    "Marta": 21
}
print("\nDiccionario inicial:", estudiantes)
estudiantes["Pedro"] = 23
estudiantes["Ana"] = 21
estudiantes.pop("Luis")
print("Diccionario actualizado:", estudiantes)
for nombre, edad in estudiantes.items():
    print(f"{nombre} tiene {edad} años")
print("Nombres:", list(estudiantes.keys()))
print("Edades:", list(estudiantes.values()))
edad_max = max(estudiantes.values())
for nombre, edad in estudiantes.items():
    if edad == edad_max:
        print(f"El/la mayor es {nombre} con {edad} años")