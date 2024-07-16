class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

class Color:
    def __init__(self, color):
        self.color = color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def calcular_area(self):
        return self.ancho * self.alto
    
cuadrado1 = Cuadrado(4, "Rojo")
print(cuadrado1.calcular_area())
print(cuadrado1.color)

    