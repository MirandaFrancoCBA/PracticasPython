class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Tipo entrada: {self.tipo_entrada}]"

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        super().__init__(marca, tipo_entrada)
        self.id_raton = Raton.contador_ratones
    
    def __str__(self) -> str:
        return f"[Id Raton: {self.id_raton} - {super().__str__()}"
    

class Teclado(DispositivoEntrada):
    contador_teclado  = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        super().__init__(marca, tipo_entrada)
        self.id_teclado = Teclado.contador_teclado

    def __str__(self) -> str:
        return f"[Id Teclado: {self.id_teclado} - {super().__str__()}"
    

    