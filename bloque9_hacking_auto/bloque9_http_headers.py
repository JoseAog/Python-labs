# bloque9_http_headers.py
import requests
import sys

def check_url(url, timeout=10):
    """Realiza una petición HEAD y GET ligera para obtener cabeceras y estado."""
    try:
        # HEAD primero (más ligero)
        head = requests.head(url, timeout=timeout)
        print(f"HEAD → Código:{head.status_code}, Tiempo: {head.elapsed.total_seconds():.3f}s")
        print("Cabeceras (HEAD):")
        for k, v in head.headers.items():
            print(f"    {k}: {v}")

        # Si HEAD no devuelve cuerpo útil, hacemos GET limitado
        if head.status_code == 200:
            get = requests.get(url, timeout=timeout, stream=True)
            print(f"\nGET → Código: {get.status_code}, Tiempo: {get.elapsed.total_seconds():.3f}s")
            content_type = get.headers.get("Content-Type", "desconocido")
            print("Content-Type:", content_type)
            # no descargamos todo el cuerpo, sólo los primero bytes
            snippet = get.raw.read(512)
            print("\nPrimeros bytes del contenido (raw):")
            try:
                print(snippet.decode("utf-8", errors="replace"))
            except Exception:
                print(repr(snippet))
            get.close()
    except requests.exceptions.RequestException as e:
        print("Error de conexión o petición:", e)

def main():
    url = input("Introduce la URL (ej: https://example.com): ").strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url
    check_url(url)

if __name__ == "__main__":
    main()