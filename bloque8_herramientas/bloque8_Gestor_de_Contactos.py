import json

ARCHIVO = "contactos.json"

# Cargar contactos
def cargar_contactos():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guardar contactos
def guardar_contactos(contactos):
    with open(ARCHIVO, "w") as f:
        json.dump(contactos, f, indent=4)

# Mostrar
def mostrar_contactos(contactos):
    if contactos:
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")
    else:
        print("No hay contactos guardados.")

# Agregar
def agregar_contacto(contactos):
    nombre = input("Nombre del contacto: ").strip()
    telefono = input("Teléfono: ").strip()
    contactos[nombre] = telefono
    guardar_contactos(contactos)
    print("Contacto agregado.")

# Menú
def menu():
    contactos = cargar_contactos()
    while True:
        print("\n--- Gestor de Contactos ---")
        print("1. Mostrar contactos")
        print("2. Agregar contacto")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_contactos(contactos)
        elif opcion == "2":
            agregar_contacto(contactos)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
