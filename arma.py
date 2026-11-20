class Arma:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

    def usar(self):
        print(f"Ataque con {self.nombre}")
        return self.daño

    