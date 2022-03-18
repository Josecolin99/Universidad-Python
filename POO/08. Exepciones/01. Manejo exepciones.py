resultado = None
a = 10
b = 0
try:
    resultado = a/b
except Exception as e:
    print(f'Ocurrio una exepcion de tipo {e}')

print(f'resultado = {resultado}')
print('Continuamos...')
