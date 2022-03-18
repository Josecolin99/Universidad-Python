from ManejoArchivos import ManejoArchivos

# with open('prueba.txt', encoding='utf8') as archivo:
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
