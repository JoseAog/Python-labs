# Funciones básicas con listas
def agregar_elemento(lista, elemento):
    lista.append(elemento)

def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)

def mostrar_lista(lista):
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

# Ejemplo de uso
mi_lista = ["manzana", "banana"]
agregar_elemento(mi_lista, "naranja")
mostrar_lista(mi_lista)
eliminar_elemento(mi_lista, "banana")
print("Lista final:", mi_lista)
