#from ..dominio.Pelicula import Pelicula
class CatalogoPeliculas:
    id_peliculas = 0
    #ruta_archivo = open("peliculas.txt", "a")
    def __init__(self):
        #CatalogoPeliculas.id_peliculas += 1
        #self.id_peliculas = CatalogoPeliculas.id_peliculas
        pass
    
    def agregar_pelicula(self, pelicula):
        #pelicula = str(input("Escriba una pelicula: "))
        self.id_peliculas += 1
        with open("peliculas.txt", "a") as arch:
            arch.write(f"ID: {self.id_peliculas} - Nombre: {pelicula}\n")
            #arch.write(str(pelicula))
    def listar_peliculas(self):
        with open("peliculas.txt", "r") as arch:
            contenido = arch.read()
            print(contenido)

    
                




