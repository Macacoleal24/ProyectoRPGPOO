class Objeto:
    def __init__(self, nombre, curacion):
        self.nombre = nombre
        self.curacion = curacion

    def usar(self, personaje):
        print(f"{personaje.nombre} usa {self.nombre}")
        personaje.curar(self.curacion)