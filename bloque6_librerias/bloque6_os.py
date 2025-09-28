import os

print("Directorio actual:", os.getcwd())
print("Archivos en el directorio:", os.listdir())

nuevo_dir = "carpeta_prueba"
if not os.path.exists(nuevo_dir):
    os.mkdir(nuevo_dir)
    print(f"Carpeta '{nuevo_dir}' creada.")
