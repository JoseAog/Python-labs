import requests
def obtener_datos_github(usuario):
    url = f"https://api.github.com/users/{usuario}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return {
            "Nombre": datos.get("name", "No disponible"),
            "Repositorios": datos.get("public_repos", 0),
            "Seguidores": datos.get("followers", 0)
        }
    except requests.exceptions.HTTPError:
        print("Usuario no encontrado en GitHub")
    except requests.exceptions.RequestException as e:
        print("Error de conexion", e)
def main():
    usuario = input("Ingresa el nombre de usuario de GitHub: ").strip()
    info = obtener_datos_github(usuario)
    if info:
        print("\n--- Informacion de GitHub ---")
        for k, v in info.items():
            print(f"{k}: {v}")
if __name__ == "__main__":
    main()