"""Ejercicio de herencia"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Vehiculo: Color {self.color}, cantidad de ruedas: {self.ruedas}. "
        

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f"{super().__str__()} Velocidad: {self.velocidad} K/h"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)   
        self.tipo = tipo     
    
    def __str__(self):
        return f"{super().__str__()} Tipo de bicicleta: {self.tipo}"

auto1 = Auto("Rojo", 4, 120)
print(auto1)

bicicleta1 = Bicicleta("Azul", 3, "Montaña")
print(bicicleta1)