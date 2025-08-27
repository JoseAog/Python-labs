import os
carpeta = input("Introduce la ruta de la carpeta que quieres organizar: ")
for archivo in os.listdir(carpeta):
    print(f"Analizando: {archivo}")
    ruta_archivo = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta_archivo):
        nombre, extension = os.path.splitext(archivo)
        extension = extension[1:]
        carpeta_destino = os.path.join(carpeta, extension.upper())
        if not os.path.exists(carpeta_destino):
            os.mkdir(carpeta_destino)
            print(f"Carpeta creada: {carpeta_destino} ")
        nueva_ruta = os.path.join(carpeta_destino,archivo)
        os.rename(ruta_archivo, nueva_ruta)
        print(f"{archivo} → {carpeta_destino}")
print("Organizacion completada. ")