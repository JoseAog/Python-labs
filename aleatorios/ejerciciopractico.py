def registrar_usuario(nombre, edad=18,*habilidades, **extra):
    print(f"Registrando usuario: {nombre}")
    print(f"Edad: {edad}")
    if habilidades:
        print("Habilidades registradas:")
        for h in habilidades:
            print(f"- {h}")
    else:
        print("No se registraron habilidades.")
    if extra:
        print("Informacion extra:")
        for clave, valor in extra.items():
            print(f"{clave}: {valor}")
    else:
        print("No se agrego informacion extra.")
    return nombre, edad, list(habilidades), extra
usuario = registrar_usuario(
    "Cristi",
    31,
    "Python", "Ciberseguridad",
    ciudad="Palma del Rio",
    premium=True
)
print("\nValores devueltos por la funcion:")
print(usuario)