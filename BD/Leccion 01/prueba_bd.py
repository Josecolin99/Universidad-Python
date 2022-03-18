import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='195929',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentecia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves_primarias = ((1, 2, 3), )
            entrada = input('Proporciona los id\'s (separado por comas) ')
            llaves_primarias = (tuple(entrada.split(',')), )
            cursor.execute(sentecia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Error tipo {e}')

finally:
    conexion.close()
