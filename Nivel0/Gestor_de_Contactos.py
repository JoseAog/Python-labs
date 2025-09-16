import json

archivo = "contactos.json"

# Cargar contactos existentes
try:
    with open(archivo, "r") as f:
        contactos = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    contactos = {}

def mostrar_contactos():
    if contactos:
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")
    else:
        print("No hay contactos guardados.")

def agregar_contacto():
    nombre = input("Nombre del contacto:").strip()
    telefono = input("Teléfono:").strip()
    contactos[nombre] = telefono
    guardar_contactos()
    print("Contacto agregado.")

def guardar_contactos():
    with open(archivo, "w") as f:
        json.dump(contactos, f, indent=4)

# Menú principal
while True:
    print("\n--- Gestor de Contactos ---")
    print("1. Mostrar contactos")
    print("2. Agregar contacto")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        mostrar_contactos()
    elif opcion == "2":
        agregar_contacto()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intenta de nuevo.")