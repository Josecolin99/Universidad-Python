class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'\n\nMonitor: Id: {self._idMonitor}\nMarca: {self._marca}, Tamaño: ' \
               f'{self._tamaño}'

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca


if __name__ == '__main__':
    monitor1 = Monitor("Benq", "17'")
    print(monitor1)
    monitor2 = Monitor("Zoowie", "23'")
    print(monitor2)
