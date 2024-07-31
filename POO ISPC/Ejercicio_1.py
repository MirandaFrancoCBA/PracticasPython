"""1. Persona. crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:
a. Un constructor, donde los datos pueden estar vacíos.
b. Los setters y getters para cada uno de los atributos. Hay que validar las
entradas de datos.
c. mostrar(): Muestra los datos de la persona.
d. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
Además, crea en una aplicación de consola que permita al usuario crear un objeto
Persona y evaluar si es mayo o menor de edad.."""

class Persona:
    def __init__(self, nombre = "", edad = 0, DNI = 0):
        self._nombre = nombre
        self._edad = edad
        self._DNI = DNI

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if nombre != "":
            self._nombre = nombre
        else: 
            print("Nombre incorrecto.")

    @property 
    def edad(self):
        return self._edad 
    @edad.setter
    def edad(self, edad):
        self._edad = edad       

    @property
    def DNI(self):
        return self._DNI
    @DNI.setter
    def DNI(self, DNI):
        self._DNI = DNI
    