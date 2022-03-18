from NumerosIdenticosExeption import NumerosIdenticosExeption

resultado = None
# Las variables dentro del bloque try except son variables locales y no pueden
# Usarse afuera
try:
    a = int(input("Dame el numero 1 "))
    b = int(input("Dame el numero 2 "))
    if a == b:
        raise NumerosIdenticosExeption("Numeros Identicos mano")
    resultado = a/b
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - Ocurrio una exepcion de tipo {zde} {type(zde)}')
except TypeError as te:
    print(f'TypeError - Ocurrio una exepcion de tipo {te} {type(te)}')
except Exception as e:
    print(f'Exception - Ocurrio una exepcion de tipo {e} {type(e)}')
else:
    print("Se arroja solo si no pasa una exepción")
finally:
    print("Se ejecuta siempre al terminar todos los bloques")

print(f'resultado = {resultado}')
print('Continuamos...')
