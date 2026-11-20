from arma import Arma
from objeto import Objeto
from personaje import Personaje

espada = Arma("Espada de hierro", 12)
heroe = Personaje("Link", 100, espada)

heroe.inventario.agregar(Objeto("Poscion pequeña", 20))
heroe.inventario.listar()
heroe.atacar()

arco = Arma("Arco de madera", 8)
heroe.arma = arco
heroe.atacar()
