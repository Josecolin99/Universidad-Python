class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self.__tipoEntrada = tipoEntrada
        self.__marca = marca

    def __str__(self):
        return f'Tipo de entrada: {self.__tipoEntrada}, Marca: {self.__marca}\n'

    @property
    def tipoEntrada(self):
        return self.__tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self.__tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca


if __name__ == '__main__':
    entrada = DispositivoEntrada('USB', 'Acer')
    print(entrada)
