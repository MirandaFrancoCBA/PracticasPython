from Producto import Producto
from Orden import Orden

producto1 = Producto("Maceta", 10)

producto2 = Producto("Jarron", 20)
producto3 = Producto("Macetita", 30)
producto4 = Producto("Colgante", 40)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
print(orden1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f"Total Orden 1 : {orden1.sumar_total()}")
orden2 = Orden(productos2)
print(orden2)
print(orden2.sumar_total())