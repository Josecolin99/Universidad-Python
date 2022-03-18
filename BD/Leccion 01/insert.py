import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='195929',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(' \
                        '%s, %s, %s)'
            valores = (
                ('Marcos', 'Cantu', 'mcantu@gmail.com'),
                ('Angeles', 'Quintana', 'aquintana@gmail.com'),
                ('Maria', 'Gonzales', 'mgonzales@gmail.com')
            )
            # execute es para un solo registro
            cursor.executemany(sentencia, valores)
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registos Insertados: {registros_insertados}')
except Exception as e:
    print(f'Error tipo {e}')

finally:
    conexion.close()