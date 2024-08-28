def codificador(texto):
    for caracter in texto:
        valor_ascii = ord(caracter)
        binario = bin(valor_ascii)
        print(binario)

def decodificador():
    pass

codificador("Hola")
