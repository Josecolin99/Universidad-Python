class Caja:
    def __init__(self, ancho, alto, largo):
        self.ancho = ancho
        self.alto = alto
        self.largo = largo

    def volumen(self):
        return self.ancho * self.alto * self.largo


ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto; "))
largo = int(input("Ingrese el largo: "))

caja = Caja(largo, ancho, alto)
print("El volumen es: ", caja.volumen())
