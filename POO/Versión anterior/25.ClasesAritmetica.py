class Aritmetica:
    """Clase aritmetica para realizar las operaciones de suma, resta, etc"""

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    """Se realiza la operación con los atributos de la clase"""

    def sumar(self):
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def dividir(self):
        return self.operando1 / self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2
        return self.operando1 % self.operando2


# Creamos un nuevo objeto
aritmetica = Aritmetica(8.5, 4)
print("Resultado de la suma: ", aritmetica.sumar())
print("Resultado de la resta: ", aritmetica.restar())
print(f"Resultado de la divición: {aritmetica.dividir():.2f}")
print("Resultado de la multiplicación: ", aritmetica.multiplicar())
