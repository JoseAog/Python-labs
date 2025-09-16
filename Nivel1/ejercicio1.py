import os
# os → funciones para manejar directorios, rutas, archivos

import subprocess
# subprocess → para ejecutar comandos externos

print("=== Script de práctica con os y subprocess ===")

# 1. Mostrar carpeta actual
print("\nCarpeta actual:", os.getcwd())
# os.getcwd() → devuelve la ruta de trabajo actual

# 2. Crear carpeta nueva si no existe
carpeta = "test_dir"
if not os.path.exists(carpeta):
    os.mkdir(carpeta)
    print(f"\nCarpeta '{carpeta}' creada.")
else:
    print(f"\nLa carpeta '{carpeta}' ya existía.")

# 3. Listar archivos en la carpeta
print("\nArchivos dentro de la carpeta actual:")
print(os.listdir("."))

# 4. Ejecutar un comando del sistema (ping)
print("\nEjecutando ping a google.com...")

# Adaptar según el sistema operativo
if os.name == "nt": # Windows
    comando = ["ping", "-n", "2", "google.com"]
else: # Linux / macOS
    comando = ["ping", "-c", "2", "google.com"]
try:
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\nResultado del ping:\n", resultado.stdout)

    # 5. Guardar en archivo de log
    with open("ping_log.txt", "w") as log:
        log.write(resultado.stdout)
    print("\nEl resultado del ping se guardó en ping_log.txt")

except Exception as e:
    print("Error ejecutando ping:", e)