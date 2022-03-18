from monitor import Monitor
from teclado import Teclado
from raton import Raton
from computadora import Computadora


class Orden:
    contadorOrdenes = 0

    def __init__(self, *computadoras):
        Orden.contadorOrdenes += 1
        self.id = Orden.contadorOrdenes
        self.computadoras = list(computadoras)
        self.separador = ''.center(70, "+")

    def agregarComputadora(self, computadoraExtra):
        self.computadoras.append(computadoraExtra)

    def __str__(self):
        computadoras_str = ''
        for i in self.computadoras:
            computadoras_str += i.__str__()
        return f'{self.separador}\n' \
               f'Orden numero {self.id}' \
               f'{computadoras_str}\n' \
               f'{self.separador}'


if __name__ == '__main__':
    monitor1 = Monitor("Benq", 22)
    monitor2 = Monitor("Zoowie", 50)

    teclado1 = Teclado("USB", "Razer")
    teclado2 = Teclado("Wirless", "Logitech")

    raton1 = Raton("USB", "Logitech")
    raton2 = Raton("USB", "PerfectMouse")

    compu = Computadora(monitor1, teclado1, raton1)
    # print(compu)
    compu.monitor = monitor2
    compu.teclado = teclado2
    compu.raton = raton2
    compu2 = Computadora(monitor2, teclado1, raton2)
    # print(compu)

    orden = Orden(compu, compu2)
    print(orden)
    orden2 = Orden(compu2, compu2)
    print(orden2)