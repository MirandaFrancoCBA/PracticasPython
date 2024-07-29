try:

    archivo = open("prueba.txt", "w")
    archivo.write("Se agrega texto llamando al metodo write \n")
    archivo.write("Aparentemente cada linea que esrcibo en archivo.write(), aparece en una linea nueva \n")
    archivo.write("Confirmó, no salta de linea si no pones barra n ")
except Exception as e:
    print(e)
finally:
    archivo.close()