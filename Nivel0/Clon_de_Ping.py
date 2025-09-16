import random
import time

print("===Clon de Ping en Python ===")

# Manejo de entradas con try/except
while True:
    host = input("Ingresa la dirección IP o host a 'pingear': ")
    if host.strip() != "":
        break
    print("Error: Debes ingresar un host válido.")
while True:
    try:
        intentos = int(input("Número de intentos: "))
        if intentos > 0:
            break
        else:
            print("El número de intentos debe ser mayor que 0.")
    except ValueError:
        print("Error: ingresa una número entero.")

# Abrimos archivo para guardar logs
with open("ping_log.txt", "w") as log_file:
    for i in range(1, intentos + 1):
        print(f"Intento {i} a {host} ...")
        tiempo = random.randint(20, 120)

        if random.random() < 0.1: # 10% de probabilidad de fallo
            mensaje = "¡Tiempo de espera agotado!"
            print(mensaje)
        else:
            mensaje = f"Respuesta desde {host}: tiempo={tiempo}ms"
            print(mensaje)

        log_file.write(f"Intento {i}: {mensaje}\n")
        time.sleep(1) # pausa 1 segundo entre intentos

print("=== Ping finalizado ===")
print("Resultados guardados en 'ping_log.txt'")