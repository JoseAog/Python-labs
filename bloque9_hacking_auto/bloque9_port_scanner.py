# bloque9_port_scanner.py
import socket
import time

def escanear_puerto(host, puerto, timeout=0.5):
    """Devuelve True si el puerto está abierto, False si está cerrado."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            res = s.connect_ex((host, puerto))
            return res == 0
        except socket.gaierror:
            raise
        except Exception:
            return False
        
def escanear_rango(host, desde=1, hasta=1024, timeout=0.25):
    abiertos = []
    inicio = time.time()
    for puerto in range(desde, hasta + 1):
        if escanear_puerto(host, puerto, timeout):
            abiertos.append(puerto)
    dur = time.time() - inicio
    return abiertos, dur

def main():
    print("Mini escáner de puertos (educativo), USO RESPONSABLE OBLIGATORIO.")
    print("Solo escanea objetivos tuyos o con permiso explícito.")
    host = input("Host (IP o dominio) [por defecto: localhost]: ").strip() or "localhost"
    try:
        desde = int(input("Puerto desde (ej.1) [por defecto 1]: ") or "1")
        hasta = int(input("Puerto hasta (ej. 1024) [por defecto 1024]: ") or "1024")
    except ValueError:
        print("Entrada inválida. Usando rago 1-1024.")
        desde, hasta = 1, 1024

    # Seguridad: limitar tamaño del rango por defecto
    if (hasta - desde) > 2000:
        print("Rango demasiado grande. Limitando a 2000 puertos desde el inicio.")
        hasta = desde + 2000

    print(f"Escaneando {host} del puerto {desde} al {hasta}...")
    try:
        abiertos, dur = escanear_rango(host, desde, hasta, timeout=0.2)
        print(f"Puertos abiertos ({len(abiertos)} encontrados) en {dur:.2f}s: {abiertos}")
    except socket.gaierror:
        print("No se pudo resolver el host. Verifica el dominio/IP.")
    except PermissionError:
        print("Permiso denegado para la operación de red.")
    except Exception as e:
        print("Error durante el escaneo:", e)

if __name__ == "__main__":
    main()

    
