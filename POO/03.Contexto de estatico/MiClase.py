class MiClase:
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_instancia)
        print(self.variable_clase)


print(MiClase.variable_clase)
print(f'Primera instancia'.center(50, '-'))
miClase = MiClase('Valor variable de instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)
print(f'Segunda instancia'.center(50, '-'))
miClase2 = MiClase('Otro valor de la clase')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
print(f'Creacion de variables de vuelo'.center(50, '-'))
# Variables de clase creadas con codigo.
MiClase.variable_clase2 = 'Variable de clase 2'
print(MiClase.variable_clase2)
print(miClase.variable_clase2)
print(miClase2.variable_clase2)
print(f'Metodo estatico'.center(50, '-'))
MiClase.metodo_estatico()
print(f'Metodo de clase'.center(50, '-'))
MiClase.metodo_clase()
miObjeto1 = MiClase("Variable de instancia desde class method")
miObjeto1.metodo_clase()
print(f'Metodo de instancia'.center(50, '-'))
miObjeto1.metodo_instancia()