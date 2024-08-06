from dominio.Pelicula import Pelicula
class CatalogoPeliculas:
    id_peliculas = 0
    ruta_archivo = open("peliculas.txt", "r")
    def __init__(self):
        CatalogoPeliculas.id_peliculas += 1
        self.id_peliculas = CatalogoPeliculas.id_peliculas
    
    def agregar_pelicula(self):
        #pelicula = str(input("Escriba una pelicula: "))
        with open("peliculas.txt", "a"):
            self.ruta_archivo.write(f"{Pelicula.nombre}")

    def listar_peliculas(self):
        with open("peliculas.txt", "r"):
            print(self.ruta_archivo.read())
                

pelicula1 = Pelicula("Batman")
print(pelicula1)

