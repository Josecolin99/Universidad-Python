from Productos import Productos
from Orden import Orden

producto1 = Productos('Camisa', 100.00)
producto2 = Productos('Pantalon', 150.00)
producto3 = Productos("Calcetines", 50.00)
producto4 = Productos("Blusa", 70.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
orden2 = (Orden(productos2))
print(orden2)