from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    print(objeto.mostar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)
print("".center(50, "-"))
gerente = Gerente('Luis', 60000, 'Sistemas')
imprimir_detalles(gerente)
