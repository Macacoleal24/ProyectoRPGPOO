from inventario import Inventario

class Personaje:
    def __init__(self, nombre, salud, arma):
        self.nombre = nombre
        self.salud = salud
        self.arma = arma  #tiene un arma
        self.inventario = Inventario()   #tiene un inventario

    def atacar(self):
        daño = self.arma.usar()
        print(f"{self.nombre} causa {daño} de daño")

    def recibir_daño(self, cantidad):
        self.salud -= cantidad
        if self.salud < 0:
            self.salud = 0
        print(f"{self.nombre} recibe {cantidad} de daño. Vida: {self.salud}")

    def curar(self, cantidad):
        self.salud += cantidad
        print(f"{self.nombre} recupera {cantidad} de vida. Vida: {self.salud}")

    def esta_vivo(self):
        return self.salud > 0