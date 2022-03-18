from monitor import Monitor
from teclado import Teclado
from raton import Raton


class Computadora:
    contadorComputadoras = 0

    def __init__(self, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.id = Computadora.contadorComputadoras
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        self._separador = ''.center(50,"-")

    def __str__(self):
        return f'\nComputadora: Id: {self.id}{self._monitor.__str__()}' \
               f'{self._teclado.__str__()}{self._raton.__str__()}\n' \
               f'{self._separador}'

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._monitor

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton


if __name__ == '__main__':
    monitor1 = Monitor("Benq", 22)
    monitor2 = Monitor("Zoowie", 50)

    teclado1 = Teclado("USB", "Razer")
    teclado2 = Teclado("Wirless", "Logitech")

    raton1 = Raton("USB", "Logitech")
    raton2 = Raton("USB", "PerfectMouse")

    compu = Computadora(monitor1, teclado1, raton1)
    print(compu)
    compu.monitor = monitor2
    compu.teclado = teclado2
    compu.raton = raton2
    print(compu)
