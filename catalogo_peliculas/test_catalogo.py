from dominio.Pelicula import Pelicula
from servicios.CatalogoPelicula import CatalogoPeliculas

pelicula1 = Pelicula("Superman")
print(pelicula1)
catalogo1 = CatalogoPeliculas
catalogo1.agregar_pelicula(pelicula1)
catalogo1.listar_peliculas()