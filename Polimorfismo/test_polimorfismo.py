from Empleado import * 
from Gerente import * 

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))


empleado1 = Empleado("Juan", 20000)
imprimir_detalles(empleado1)
empleado2 = Gerente("Jose", 50000, "Cobranzas")
imprimir_detalles(empleado2)
