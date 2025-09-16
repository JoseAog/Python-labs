import os
import subprocess
from datetime import datetime

print("=== Mini Reto: Explorador + Ping con fecha/hora ===")

# 1. Mostrar carpeta actual
print("Carpeta actual:", os.getcwd())

# 2. Crear carpeta nueva llamada 'reto_dir' si no existe
carpeta = "reto_dir"
if not os.path.exists(carpeta): 
    os.mkdir(carpeta)
    print(f"Carpeta '{carpeta}' creada.")
else:
    print(f"La carpeta '{carpeta}' ya existía.")

# 3. Listar archivos en la carpeta actual
print("Archivos dentro de la carpeta actual:")
print(os.listdir("."))

# 4 . Ejecutar ping a google.com
if os.name == "nt": # Windows
    comando = ["ping", "-n", "2", "google.com"]
else: # Linux / macOS
    comando = ["ping", "-c", "2", "google.com"]
try:
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\nResultado del ping: \n", resultado.stdout)

    # 5. Guardar el resultado en 'reto_ping_log.txt' con fecha/hora
    ahora = datetime.now()
    with open("reto_ping_log.txt", "w") as log:
        log.write(f"Ping ejecutado el: {ahora.strftime('%Y-%m-%d %H:%M:%S')} \n")
        log.write(resultado.stdout) 
    print("\nResultado guardado en 'reto_ping_log.txt' con fecha y hora")

except Exception as e:
    print("Error ejecutando ping:", e)