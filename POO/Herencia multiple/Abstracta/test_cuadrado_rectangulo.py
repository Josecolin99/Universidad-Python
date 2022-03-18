from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación Objeto Cuadrado'.center(50, '-'))
cuadrdo1 = Cuadrado(5, "azul")
print(cuadrdo1)
cuadrdo1.alto = 30
print(cuadrdo1)
print('Creación Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(9, 1, "Amarillo")
print(rectangulo1)
rectangulo1.ancho = 8
print(rectangulo1)