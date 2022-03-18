archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())

# Leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))
# print(archivo.read(3))


# Leer linas completas

# print(archivo.readline())
# print(archivo.readline())

# Iterar el archivo
# for linea in archivo:
#   print(linea)


# Leer lineas
# print(archivo.readlines())

# Acceder a una lina de la lista
# print(archivo.readlines()[0])


# abrimos un nuevo archivo y copiamos
# a anexar
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write((archivo.read()))

archivo.close()
archivo2.close()
