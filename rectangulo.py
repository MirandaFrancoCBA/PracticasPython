from herenciaMultiple import *

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, base, altura, color):
        FiguraGeometrica.__init__(self, base, altura)
        Color.__init__(self, color)
    
    def calcular_area_rectangulo (self):
        return f"El Area del rectangulo es: {self.ancho * self.alto}" 
    
    def __str__(self):
        return f" [Base: {self.ancho}  Altura: {self.alto} {Color.__str__(self)}]" 

rectangulo1 = Rectangulo(5, 10, "Rojo")

print(rectangulo1)
print(rectangulo1.calcular_area_rectangulo())
        