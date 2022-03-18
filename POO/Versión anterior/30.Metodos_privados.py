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

    def get_apellido_materno(self):
        return self.__apellido_materno

    def set_apellido_materno(self, ape_materno):
        self.__apellido_materno = ape_materno


p1 = Persona("Juan", "Lopez", "Perez")
# p1.metodo_privado() no se puede acceder debido a que es un metodo privado
p1.metodo_publico()

print(p1.nombre)

# Se puedem acceder pero no se recomienda, al menos que sea por
# metodo get o set
print(p1._apellido_paterno)

# print(p1.__apellido_materno) manda un error por ser privado
p1.set_apellido_materno("Najera")
print(p1.get_apellido_materno())
