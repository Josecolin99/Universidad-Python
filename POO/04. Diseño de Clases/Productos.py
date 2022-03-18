class Productos:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Productos.contador_productos += 1
        self._id_producto = Productos.contador_productos
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f'Id: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

    @property
    def precio(self):
        return self._precio


if __name__ == '__main__':
    producto1 = Productos('Camisa', 100.00)
    print(producto1)
    producto2 = Productos('Pantalon', 150.00)
    print(producto2)