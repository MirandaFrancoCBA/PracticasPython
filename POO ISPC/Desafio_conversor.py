"""Conversor de Monedas. Crea una clase Moneda que permita la conversión
entre monedas (ej. dólares a pesos). Implementa los métodos __str__ y
__add__ para mostrar la cantidad convertida y sumar cantidades en
diferentes monedas."""

class Moneda:
    tipo_cambio = {"USD":1450, "EUR":1500}
    def __init__(self, cantidad, moneda):
        self.cantidad = cantidad
        self.moneda = moneda

    def convertir(self):
        moneda_upper = self.moneda.upper()
        try:
            moneda_upper in self.tipo_cambio
            return f"{self.tipo_cambio[moneda_upper] * self.cantidad} pesotes amigo!"
        except Exception:
            print("Moneda no soportada")

    def __str__(self):
        return f"Convertimos {self.cantidad} {self.moneda.upper()} a pesos argentos"
    
mon1 = Moneda(100, "USD")
print(mon1)
print(mon1.convertir())
    

    
