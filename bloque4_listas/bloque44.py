A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.add(7)
B.update([7, 8, 9])
A.remove(2)
B.discard(10)
union = A | B
interseccion = A & B
diferencia = A - B
deferencia_simetrica = A ^ B
print(A)
print(B)
print(5 in A)
print(7 in B)
print(A.issubset(B))
print(A.issuperset(B))
print("Elementos de A:")
for elem in A:
    print(elem)
print(len(B))
B.clear()
print(B)