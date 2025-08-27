import os
carpeta = input("Ruta: ")
if os.path.exists(carpeta):
    print("Archivos encontrados: ")
    for archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta):
            nombre, ext = os.path.splitext(archivo)
            print(f"{archivo} → Nombre: {nombre}, Extension {ext}")
else:
    print("Carpeta no encontrada")