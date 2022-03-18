import psycopg2 as bd

conexion = bd.connect(user='postgres',
                      password='195929',
                      host='127.0.0.1',
                      port='5432',
                      database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona(nombre, apellido, email) ' \
                        'VALUES(%s,%s,%s)'
            valores = ('Maria', 'Esparza', 'mesparza@mail')
            cursor.execute(sentencia, valores)
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s ' \
                        'WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail', 10)
            cursor.execute(sentencia, valores)
except Exception as e:
    print(f'Hay un rollback mano {e}')
finally:
    conexion.close()
print('Termina la transaccion, commit ok')
