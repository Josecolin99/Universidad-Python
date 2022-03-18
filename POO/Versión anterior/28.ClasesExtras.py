class Personas:
    # Se puede ocupar otro nombre que no sea self, pero es lo mas comun
    # y recomendable.
    # Pero se pude poner otro nombre si de ese modo se quiere
    # Los nombres no tiene que ser iguales cuando se crea el argumento de
    # clases

    def __init__(this, n, e, *v, **d):  # Para agregar una tupla es * y un nombre y se vuelve un parametro opcional
        this.nombre = n  # Para un diccionario es con doble **
        this.edad = e
        this.valores = v
        this.diccionario = d

    # Se puede combinar self y otra palabra, simepre que se respete la misma en el bloque
    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Valores(Tupla): ", self.valores)
        print("Diccionario: ", self.diccionario)


p1 = Personas("Juan", 28)
p1.desplegar()

print()

p2 = Personas("Karla", 30, 2, 4, 5)
p2.desplegar()

print()

p2 = Personas("Paola", 33, 5, 8, 5, m="manzana", p="pera")
p2.desplegar()

print()
