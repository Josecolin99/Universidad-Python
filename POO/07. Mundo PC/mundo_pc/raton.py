from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        Raton.contadorRatones += 1
        self.id = Raton.contadorRatones
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'\n\nRaton: Id: {self.id}\n{super().__str__()}'


if __name__ == "__main__":
    raton = Raton("USB", "Logitech")
    print(raton)
    raton2 = Raton("USB", "Logitech")
    print(raton2)
    raton3 = Raton("USB", "Logitech")
    print(raton3)
