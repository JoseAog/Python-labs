import requests

print("=== Ejercicio: Descargador de página web ===")

# 1. URL de la página a descargar
url = "https://www.example.com"

try:
    # 2. Hacer la petición GET
    respuesta = requests.get(url)

    # 3. Mostrar información en pantalla
    print("Código de estado:", respuesta.status_code)
    print("\nContenido de la página(primeros 300 caracteres):\n")
    print(respuesta.text[:300])

    # 4. Guardar el contenido completo en un archivo
    with open("pagina_descargada.html", "w", encoding="utf-8") as f:
        f.write(respuesta.text)
    print("\nEl contenido se guardó en 'pagina_descargada.html'")

except requests.RequestException as e:
    print("Error accediendo a la página:", e)