# Encapsulación con atributos privados
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad

    def mostrar_saldo(self):
        return f"Saldo disponible: {self.__saldo}€"

# Ejemplo de uso
if __name__ == "__main__":
    cuenta = CuentaBancaria("Carlos", 100)
    cuenta.depositar(50)
    cuenta.retirar(30)
    print(cuenta.mostrar_saldo())
