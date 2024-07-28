class Producto:
    contador_producto = 0

    def __init__(self, nombre, precio):
        Producto.contador_producto += 1
        self._id_producto = Producto.contador_producto
        self._nombre = nombre
        self._precio = precio
    
    @property
    def id_producto(self):
        return self._id_producto
    
    @id_producto.setter

    def id_producto(self, id_producto):
        self._id_producto = id_producto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter

    def nombre(self, nombre):
        self._nombre = nombre 

    @property 
    def precio(self):
        return self._precio

    @precio.setter

    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"Id Producto: {self.id_producto} - Nombre: {self.nombre} - Precio: {self.precio}"
    


        
