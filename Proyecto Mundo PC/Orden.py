from DispositivoEntrada import * 
from Monitor import * 
from Computadora import *

class Orden:
    contador_orden  = 0

    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._computadoras = list(computadoras)
    
    @property
    def id_orden(self):
        return self._id_orden
    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden

    @property
    def computadoras(self):
        return self._computadoras
    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def agregar_computadoras(self, computadora):
        self.computadoras.append(computadora)
    
    def __str__(self) -> str:
        computadoras_str = ""
        for computadora in self.computadoras:
            computadoras_str += computadora.__str__()
        
        return f""" Orden N: {self.id_orden}
        {computadoras_str}

"""



