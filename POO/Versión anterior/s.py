class Aritmetica:
    """Clase aritmetica para realizar las operaciones de suma, resta, etc"""

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    """Se realiza la operación con los atributos de la clase"""

    def sumar(self):
        return self.operando1 + self.operando2


class Aritmetica2(Aritmetica):
    def __init__(self, operando1, operando2):
        super().__init__(operando1, operando2)

    def suma(self):
        return print(f"La suma de {self.operando1} y "
                     f"{self.operando2} {super().sumar()}")


aritmetica = Aritmetica2(5, 7)

aritmetica.suma()
