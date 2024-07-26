class Persona:

    contador_persona = 0
    @classmethod
    def generar_contador_persona(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        
        self.id_persona = Persona.generar_contador_persona()
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"Persona [{self.id_persona} {self.nombre} {self.edad}]"

persona1 = Persona("Juan", 10)
print(persona1)
persona2 = Persona("Oscar", 20)
print(persona2)
persona3 = Persona("Lucas", 23)
print(persona3)
