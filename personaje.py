from inventario import Inventario

class Personaje:
    def __init__(self, nombre, salud, arma):
        self.nombre = nombre
        self.salud = salud
        self.arma = arma
        self.inventario = Inventario()
        