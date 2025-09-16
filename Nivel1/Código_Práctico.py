import os
import subprocess

print("=== Demo librerías os y subprocess ===")

# Usando os para listar archivos en el directorio actual
print("\n[os.listdir()] Archivos en esta carpeta:")
print(os.listdir("."))

# Usando os para obtener la ruta actual
print("\n[os.getcwd()] Ruta actual:")
print(os.getcwd())

# Usando subprocess para ejecutar un comando del sistema
print("\n[subprocess.run()] Ejecutando 'ping -c 1 google.com' (Linux/macOS)")
try:
    resultado = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True)
    print(resultado.stdout)
except Exception as e:
    print("Error ejecutando ping:", e)