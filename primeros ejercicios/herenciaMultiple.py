class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property

    def ancho(self):
        return self._ancho

    @ancho.setter

    def ancho(self, ancho):
        self._ancho = ancho

    @property

    def alto(self):
        return self._alto
    @alto.setter

    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f"Figura Geometrica [Ancho: {self._ancho} Alto: {self._alto} ]"


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
        return f"Color: {self._color}"

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)} {Color.__str__(self)}"

    
cuadrado1 = Cuadrado(4, "Rojo")
print(cuadrado1)
print(cuadrado1.calcular_area())
    