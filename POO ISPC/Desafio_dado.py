"""Intenta crear una clase Dado que cumpla los siguientes
requerimientos:
● el dado debe tener un número de caras (por defecto 6)
● debe ser capaz de lanzarse y devolver un número aleatorio entre 1
y el número de caras."""
from random import randint
class Dado:
    def __init__(self, caras = 6):
        self.caras = caras
    
    def lanzar_dado(self):
        return randint(1, self.caras)
    
dado1 = Dado(6)
print(f"Lanzaste el dado y el numero fue: {dado1.lanzar_dado()}")
dado2 = Dado()
print(f"Este dado tiene por defecto 6 caras. Tu numero es: {dado2.lanzar_dado()}")

dado3 = Dado(int(input("Ingresa un numero de caras: ")))
print(f"Tu dado cayo en: {dado3.lanzar_dado()}")