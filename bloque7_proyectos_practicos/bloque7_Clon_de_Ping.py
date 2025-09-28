import os
import subprocess
from datetime import datetime

print("=== Clon de ping ===")

if os.name == "nt":  # Windows
    comando = ["ping", "-n", "2", "google.com"]
else:  # Linux / macOS
    comando = ["ping", "-c", "2", "google.com"]

try:
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\nResultado del ping:\n", resultado.stdout)

    # Guardar log con fecha
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ping_log.txt", "a", encoding="utf-8") as log:
        log.write(f"Ping ejecutado el {ahora}\n")
        log.write(resultado.stdout + "\n")
    print("\nResultado guardado en 'ping_log.txt'")

except Exception as e:
    print("Error ejecutando ping:", e)
