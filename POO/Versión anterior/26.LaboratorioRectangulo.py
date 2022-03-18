# Mi solución 1
"""class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


rectangulo = Rectangulo(0, 0)
rectangulo.base = int(input("Ingrese la base: "))
rectangulo.altura = int(input("Ingrese la altura: "))
print("El area es: ", rectangulo.calcular_area())
"""


# Solucion 2
class RectanguloProfe:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = int(input("Proporcione la base: "))
altura = int(input("Proporcine la altura: "))

rectangulo = RectanguloProfe(base, altura)
print(rectangulo.calcular_area())

rectangulo1 = RectanguloProfe(4, 2)
print(rectangulo1.calcular_area())
