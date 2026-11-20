class Combate:
    def __init__(self, jugador, enemigo):
        self.jugador = jugador
        self.enemigo = enemigo

    def turno_jugador(self):
        while True:
            print("\n1. Atacar")
            print("2. Usar objeto")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                daño = self.jugador.atacar()
                self.enemigo.recibir_daño(daño)
                return
            elif opcion == "2":
                if self.jugador.inventario.esta_vacio():
                    print("No tienes objetos")
                    continue
                self.jugador.inventario.listar()
                numero = int(input("Número del objeto: "))
                objeto = self.jugador.inventario.sacar(numero)
                objeto.usar(self.jugador)
                return
            else:
                print("Opción inválida")

    def turno_enemigo(self):
        print(f"\nTurno de {self.enemigo.nombre}")
        daño = self.enemigo.atacar()
        self.jugador.recibir_daño(daño)

    def iniciar(self):
        print(f"\n¡{self.jugador.nombre} contra {self.enemigo.nombre}!")
        while self.jugador.esta_vivo() and self.enemigo.esta_vivo():
            self.turno_jugador()
            if self.enemigo.esta_vivo():
                self.turno_enemigo()

        if self.jugador.esta_vivo():
            print(f"\n¡{self.jugador.nombre} gana!")
        else:
            print(f"\n{self.jugador.nombre} ha caído...")
        return self.jugador.esta_vivo()