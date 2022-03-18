from Persona import Persona

print('Creación de objetos'.center(50, '-'))
persona1 = Persona('Corina', 'Najera', 50)
persona1.mostrar_detalle()

print('Eliminación de objetos'.center(50, '-'))
del persona1
