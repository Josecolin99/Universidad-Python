# Se encapsulan los datos, para que solo se puedan modificar dentro de
# la clase, se pone una variable privada con __ y se tienen que llamar y
# modificar dentro de su clase, con el metodo get y set, se pueden llamar
# de otra forma pero llamarlo asi es una buena practica de programacion
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad  # Semi privadas

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre


p1 = Persona("Juan", 18)
# print(p1.__nombre) marca un error
print(p1.get_nombre())
print(p1._edad)  # Llamada de una variable semi provada
# p1.nombre = "Karla" marca un error
# print(p1.__nombre) marca un error

p1.set_nombre("Karla")
p1._edad = 21
print(p1.get_nombre())
print(p1._edad)  # Print de una variable semi privada
