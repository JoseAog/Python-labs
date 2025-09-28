# Ejemplo de funciones y argumentos
def registrar_usuario(nombre, edad=18, *habilidades, **info_extra):
    print(f"Registrando usuario: {nombre}")
    print(f"Edad: {edad}")
    
    if habilidades:
        print("Habilidades registradas:")
        for h in habilidades:
            print(f"- {h}")
    else:
        print("No se registraron habilidades.")
    
    if info_extra:
        print("Información extra:")
        for clave, valor in info_extra.items():
            print(f"{clave}: {valor}")
    
    return nombre, edad, list(habilidades), info_extra

# Ejemplo de uso
usuario = registrar_usuario(
    "Cristi",
    31,
    "Python", "Ciberseguridad",
    ciudad="Palma del Rio",
    premium=True
)
print("\nValores devueltos por la función:")
print(usuario)
