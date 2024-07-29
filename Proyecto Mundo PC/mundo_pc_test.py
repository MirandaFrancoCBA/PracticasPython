from DispositivoEntrada import * 
from Monitor import * 
from Computadora import * 
from Orden import *


teclado1 = Teclado("HP", "USB")
raton1 = Raton("HP", "Bluetooth")
monitor1 = Monitor("Samsung", "20 Pulgadas")

computadora1 = Computadora("Acer", monitor1, teclado1, raton1)

lista1 = [computadora1]

orden1 = Orden(lista1)
print(orden1)

teclado2 = Teclado("Noga", "Bluetooth")
raton2 = Raton("Noga", "USB")
monitor2 = Monitor("Pichichu", "70 Pulgadas")

computadora2 = Computadora("Sony", monitor2, teclado2, raton2)

lista2 = [computadora2]

orden2 = Orden(lista2)
print(orden2)