
import pandas as pd
import numpy as np


#1Definir variables básicas y tipos de datos (1 punto): 
#o Crea una lista que contenga al menos cinco libros, donde cada libro sea un diccionario con los atributos título (cadena de caracteres), autor (cadena de caracteres), precio (decimal) y cantidad en stock (entero)

# Definir variables ingresadas por el usuario
titulo_libro = input("Ingrese el título del libro: ") 
autor = input("Ingrese el autor del libro: ")
cantidad_en_stock = int(input("Ingrese la cantidad en stock: "))
precio = float(input("Ingrese el precio del libro: ")) 

# Lista inicial de libros (diccionarios dentro de una lista)
libros = [
    {"titulo": "War and Peace", "autor": "Leo Tolstoy", "precio": 10.99, "cantidad_en_stock": 50},
    {"titulo": "To Kill a Mockingbird", "autor": "Harper Lee", "precio": 12.99, "cantidad_en_stock": 30},
    {"titulo": "The Great Gatsby", "autor": "F. Scott Fitzgerald", "precio": 14.99, "cantidad_en_stock": 20},
    {"titulo": "The Catcher in the Rye", "autor": "J.D. Salinger", "precio": 11.99, "cantidad_en_stock": 40},
    {"titulo": "The Hobbit", "autor": "J.R.R. Tolkien", "precio": 13.99, "cantidad_en_stock": 60}
]

# Agregar el nuevo libro a la lista
libros.append({
    "titulo": titulo_libro,
    "autor": autor,
    "precio": precio,
    "cantidad_en_stock": cantidad_en_stock
})

# Imprimir todos los libros
print("\n Lista completa de libros:")
for libro in libros:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Precio: ${libro['precio']:.2f}, Stock: {libro['cantidad_en_stock']}")


#2Control de flujo (1 punto):
#o Implementa una función llamada mostrar_libros_disponibles() que recorra la lista de libros y muestre en pantalla los libros que tienen más de una unidad en stock usando una sentencia for y una condición if.

def mostrar_libros_disponibles(libros):
    
    for libro in libros:
        if libro['cantidad_en_stock'] >= 1:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Precio: ${libro['precio']:.2f}, Stock: {libro['cantidad_en_stock']}")
        elif libro['cantidad_en_stock'] == 1:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Precio: ${libro['precio']:.2f}, Stock: {libro['cantidad_en_stock']}")
            print("Solo queda un libro en stock") 
            print("No hay libros disponibles") 
libros = [
    {"titulo": "War and Peace", "autor": "Leo Tolstoy", "precio": 10.99, "cantidad_en_stock": 50},
    {"titulo": "To Kill a Mockingbird", "autor": "Harper Lee", "precio": 12.99, "cantidad_en_stock": 30},
    {"titulo": "The Great Gatsby", "autor": "F. Scott Fitzgerald", "precio": 14.99, "cantidad_en_stock": 0},
    {"titulo": "The Catcher in the Rye", "autor": "J.D. Salinger", "precio": 11.99, "cantidad_en_stock": 1},
    {"titulo": "The Hobbit", "autor": "J.R.R. Tolkien", "precio": 13.99, "cantidad_en_stock": 60}
]

mostrar_libros_disponibles(libros)

#3Condiciones y operadores (1 punto):
# Solicita al usuario que ingrese un rango de precios (mínimo y máximo) y utiliza una sentencia if elif else para filtrar los libros en el rango ingresado y mostrarlos enpantalla

rango_precios_minimo =input("Ingrese el rango minimo de precios: ")
rango_precios_maximo = input("Ingrese el rango maximo de precios: ") 
libros = input("")

def filtrar_libros_por_precios(libros, rango_precios_minimo, rango_precios_maximo):
    for libro in libros:
        if libro['precio'] >= rango_precios_minimo and libro['precio'] <= rango_precios_maximo:
            print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Precio: ${libro['precio']:.2f}, Stock: {libro['cantidad_en_stock']}") 
        elif libro['precio'] < rango_precios_minimo and libro['precio'] > rango_precios_maximo:
            print("No hay libros en el rango de precios ingresado")
print(f"Los libros en el rango de precios ingresado son: {libro['titulo']}, {libro['autor']}, {libro['precio']}, {libro['cantidad_en_stock']}") 

#Función personalizada para simular una compra (2 puntos):
#Crea una función comprar_libros(título, cantidad) que reciba como parámetros el título del libro y la cantidad a comprar. La función debe:
#▪ Verificar si el libro está en el inventario y si la cantidad deseada está disponible.
#▪ Si la compra es válida, restar la cantidad comprada al stock y mostrar el monto total de la compra.
#▪ Si la cantidad solicitada es mayor al stock disponible, mostrar un mensaje de error


def comprar_libros(titulo, cantidad): 
    for libro in libros:
        if libro['titulo'] == titulo:
            if libro['cantidad_en_stock'] >= cantidad:
                print(f"Compra exitosa: {cantidad} unidades de '{titulo}' han sido compradas.") 
                libro['cantidad_en_stock'] -= cantidad
                print(f"Stock actulizado: {libro['cantidad_en_stock']} unidades de '{titulo}' han sido compradas.") 
                print(f"Monto total de la compra: ${libro['precio'] * cantidad:.2f}")
                return True 
            if libro['cantidad_en_stock'] < cantidad:
                print(f"No hay suficiente stock de '{titulo}'.") 
                return False
      
            print(f"Stock actual: {libro['cantidad_en_stock']} unidades de '{titulo}'") 