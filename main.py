from arma import Arma
from objeto import Objeto
from personaje import Personaje
from combate import Combate

espada = Arma("Espada de hierro", 12)
navaja = Arma("Navaja", 6)

heroe = Personaje("Link", 100, espada)
heroe.inventario.agregar(Objeto("Poción pequeña", 20))
heroe.inventario.agregar(Objeto("Poción mediana", 40))

goblin = Personaje('Goblin', 50, navaja)

combate = Combate(heroe, goblin)
combate.iniciar()
