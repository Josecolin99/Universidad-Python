from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.contadorRatones += 1
        self.id = Teclado.contadorRatones
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'\n\nTeclado = Id: {self.id}\n{super().__str__()}'


if __name__ == "__main__":
    teclado = Teclado("USB", "Logitech\n")
    print(teclado)
