class Computadora:
    contador_computadora = 0

    def __init__(self, nombre):
        Computadora.contador_computadora += 1
        self._nombre = nombre
        self._id_computadora = Computadora.contador_computadora
    
            
