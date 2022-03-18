from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Area = {self.area()}\n' \
               f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'


if __name__ == '__main__':
    cuadrado1 = Cuadrado(25, "Rojo")
    print(cuadrado1)
    cuadrado1.alto = 5
    cuadrado1.ancho = 5
    cuadrado1.color = "Azul"
    print(cuadrado1.ancho)
    print(cuadrado1.alto)
    print(cuadrado1.color)
    print(cuadrado1)
    cuadrado2 = Cuadrado(7, "Amarillo")
    print(cuadrado2)
