import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='195929',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input("Proporciona los id persona a eliminar: ")
            valores = (tuple(entrada.split(',')), )
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registos eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Error tipo {e}')

finally:
    conexion.close()
