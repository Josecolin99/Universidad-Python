from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Area del Rectangulo = {self.area()} \n' \
               f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'


if __name__ == '__main__':
    rectangulo1 = Rectangulo(10, 15, "Rojo")
    print(rectangulo1)
    rectangulo1.alto = 5
    rectangulo1.ancho = 10
    rectangulo1.color = "Azul"
    print(rectangulo1.alto)
    print(rectangulo1.ancho)
    print(rectangulo1.color)
    print(rectangulo1)
    rectangulo2 = Rectangulo(6, 8, "Amarillo")
    print(rectangulo2)
