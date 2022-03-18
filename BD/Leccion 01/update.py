import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='195929',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s ' \
                        'WHERE id_persona=%s'
            # id_persona = input("Id a actualizar: ")
            valores = (
                ('Juan', 'Perez', 'jperez@mail.com', 1),
                ('Ivonne', 'Gutierrez', 'igutierrez@mail.com', 2),
            )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registos actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Error tipo {e}')

finally:
    conexion.close()