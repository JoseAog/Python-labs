import json

persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

# Guardar en JSON
with open("persona.json", "w") as f:
    json.dump(persona, f)

# Leer JSON
with open("persona.json", "r") as f:
    datos = json.load(f)

print("Contenido leído del JSON:", datos)
