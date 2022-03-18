class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color[Color={self.color}]'


if __name__ == '__main__':
    color1 = Color("Rojo")
    print(color1)
    print(color1.color)
    color1.color = 'Azul'
    print(color1)
    print(color1.color)