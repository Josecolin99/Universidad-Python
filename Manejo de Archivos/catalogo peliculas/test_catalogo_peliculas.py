from dominio.Pelicula import Pelicula
from servicio.Catalogo_Peliculas import CatalogosPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print("""
        Opciones:
        1. Agregar Peliculas
        2. Listar Peliculas
        3. Eliminar catalogo de peliculas
        4. salir
        """)
        opcion = int(input("Escribe tu opcion (1-4) "))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error de tipo {e}')
else:
    print("Salimos del catalogo....")
