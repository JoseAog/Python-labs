import os
import shutil

print("=== Organizador de archivos por extensión ===")

carpeta = "archivos_prueba"
if not os.path.exists(carpeta):
    os.mkdir(carpeta)

# Crear subcarpetas
categorias = ["imagenes", "documentos", "otros"]
for c in categorias:
    ruta = os.path.join(carpeta, c)
    if not os.path.exists(ruta):
        os.mkdir(ruta)

# Recorrer archivos en carpeta base
for archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, archivo)

    if os.path.isfile(ruta):
        if archivo.endswith((".png", ".jpg", ".jpeg")):
            destino = os.path.join(carpeta, "imagenes", archivo)
        elif archivo.endswith((".txt", ".pdf", ".docx")):
            destino = os.path.join(carpeta, "documentos", archivo)
        else:
            destino = os.path.join(carpeta, "otros", archivo)
        shutil.move(ruta, destino)

print("Archivos organizados en sus respectivas carpetas.")
