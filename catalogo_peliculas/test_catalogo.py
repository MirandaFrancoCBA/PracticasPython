from dominio.Pelicula import Pelicula
from servicios.CatalogoPelicula import CatalogoPeliculas
import os

opcion = 0

print("¡Bienvenido al Catalogo de Peliculas!".center(50, "_"))
print("Opcion 1: Agregar pelicula".center(50, ("-")))
print("Opcion 2: Ver lista ".center(50, ("-")))
print("Opcion 3: Eliminar archivo".center(50, ("-")))
print("Opcion 4: Salir ".center(50, ("-")))

opcion = int(input("Elija una opcion (1 - 4): "))

if opcion == 4:
    exit