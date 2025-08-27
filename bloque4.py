frutas = ["manzana", "pera", "platano"]
print("Inicial:", frutas)
print("Primera:", frutas[0])
print("Ultima:", frutas[-1])
frutas[1] = "uva"
print("Tras cambio indice 1 → 'uva':", frutas)
frutas.append("kiwi")
frutas.extend(["mango", "pera"])
frutas.insert(1, "naranja")
frutas.remove("pera")
ultimo = frutas.pop()
primero = frutas.pop(0)
print("pop → ultimo:", ultimo, "|primero:", primero)
print("Frutas ahora:", frutas)
nums = [5, 2, 8, 2, 1]
nums.sort()
nums.reverse()
print("Nums orden descendente:", nums)
print("Recorrido simple:")
for fruta in frutas:
    print(" -", fruta)
print("Recorrido con indices:")
for idx, fruta in enumerate(frutas):
    print(f" {idx} → {fruta}")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Elemento [1][0]:", matriz[1][0])
matriz[0][2] = 99
print("Fila 0 tras cambio:", matriz [0])
a = [1, 2, 3]
b = a
c = a.copy()
a.append(4)
print("a:", a, "| b (misma ref):", b, "| c (copia):", c)
import copy
d = [[1, 2], [3, 4]]
shallow = d.copy()
deep = copy.deepcopy(d)
d[0][0] = 99
print("d:", d)
print("shallow (afectada):", shallow)
print("deep (intacta):", deep)
print("Veces que aparece 'uva':", frutas.count("uva"))
print("Indice de 'kiwi' :", frutas.index("kiwi"))