import requests

print("=== Ejemplo: Consumo de API de GitHub ===")

# Endpoint de ejemplo (repos públicos de un usuario)
usuario = input ("Introduce un usuario de GitHub: ").strip()
url = f"https://api.github.com/users/{usuario}/repos"

try:
    respuesta = requests.get(url)
    respuesta.raise_for_status() # Lanza error si la respuesta no es 200

    repos = respuesta.json()
    if repos:
        print(f"\nRepositorios públicos de {usuario}:")
        for repo in repos:
            print(f"- {repo['name']} (⭐ {repo['stargazers_count']})")
    else:
        print(f"\nEl usuario '{usuario}' no tiene repositorios públicos.")

except requests.exceptions.RequestException as e:
    print("Error al conectar con la API de GitHub:", e)