def calculadora(a, b, operacion="suma"):
    """Realiza suma o resta segun el parametro 'operacion'"""
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    else:
        return "Operacion no valida"
def sumar_varios(*args):
    """Suma todos los numeros que se pasen como argumentos """
    return sum(args)
def mostrar_datos(**kwargs):
    """Devuelve un diccionario con la informacion pasada"""
    return kwargs
def operaciones_completas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion
print(calculadora(5, 3))
print(calculadora(5, 3, "resta"))
print(sumar_varios(1, 2, 3, 4, 5))
print(mostrar_datos(nombre="Ana", edad=25))
s, r, m = operaciones_completas(6, 2)
print(s,r,m)