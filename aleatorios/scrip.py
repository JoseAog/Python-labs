import os
carpeta = input("Introduce la ruta de la carpeta con archivos: ")
nuevo_nombre_base = input("Nuevo nombre base para los archivos: ")
archivos = os.listdir(carpeta)
for i, archivo in enumerate(archivos):
    extension = os.path.splitext(archivo)[1]
    nuevo_nombre = f"{nuevo_nombre_base}_{i+1}{extension}"
    os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, nuevo_nombre))
print("Archivos renombrados con exito. ")