class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre  # atributo publico
        self._apellido_paterno = ape_paterno  # Protegido / parcialmente privado
        self.__apellido_materno = ape_materno  # Privado

    def metodo_publico(self):
        self.__metodo_privado()

    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)

    """
    Property es un decorador que permite crear una duncion get
    """

    @property
    def apellido_materno(self):
        return self.__apellido_materno

    """
    setter permite crear una funcion set, colocando el nombre de la funcion
    segido de un setter, fijarse en que tando la funcion property como la 
    funcion setter se llaman igual.
    """

    @apellido_materno.setter
    def apellido_materno(self, ape_materno):
        self.__apellido_materno = ape_materno


p1 = Persona("Juan", "Lopez", "Perez")
# p1.metodo_privado() no se puede acceder debido a que es un metodo privado
p1.metodo_publico()

print(p1.nombre)

# Se puedem acceder pero no se recomienda, al menos que sea por
# metodo get o set
print(p1._apellido_paterno)

"""
Gracias a la funcion sertter se puede llamar la funcion sin parentesis y 
sobrescribirlas de manera convencional
"""
p1.apellido_materno = "Najera"

"""
Lo mismo con la funicon property, no es necesario poner los ()
"""
print(p1.apellido_materno)
