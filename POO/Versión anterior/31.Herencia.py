class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # Con esto se puede llamar las variables de la clase padre
        self.sueldo = sueldo

    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)


persona = Persona("Juan", 28)
print(persona)

empleado = Empleado("Karla", 30, 500.0)

print(empleado)

empleado.nombre = "Karla Ivone"
empleado.sueldo = "1000.00"

print(empleado)
