class Orden:

    contador_orden = 0

    def __init__(self, productos):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)

    @property
    def id_orden(self):
        return self._id_orden
    
    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden
    
    @property 
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, productos):
        self._productos = productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def sumar_total(self):
        total = 0

        for producto in self.productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ""

        for producto in self.productos:
            productos_str += producto.__str__() + "-"

        return f"Orden: {self.id_orden}, \nProductos: {productos_str}"

