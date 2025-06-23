#2.5. Equipo 5: Análisis de Impacto de Descuentos
#1. Cree una matriz de 4 × 5 con las ventas semanales de los cinco productos en las cuatro tiendas (valores enteros entre 10 y 60). 
# Haga una copia de esta matriz y aplique un descuento del 15% a todas las ventas en la copia. 
# Verifique si la matriz original permanecesin cambios y calcule la diferencia total en ingresos debido al descuent

import math

#matriz 4 x 5
matriz_ventas = [[0] * 5 for _ in range(4)]

#generar ventas aleatorias
import random

# Crear una matriz vacía de 4x5
matriz_ventas = []

# Generar ventas aleatorias
for i in range(4):
    fila = []
    for j in range(5):
        venta = random.randint(10, 60)
        fila.append(venta)
        print(f"Venta en fila {i}, columna {j}: {venta}")
    matriz_ventas.append(fila)
    print("\n")  # Salto de línea después de cada fila 

#copiar matriz
matriz_copia = [row[:] for row in matriz_ventas]
print(matriz_copia)

#aplica descuento del 15%
if matriz_copia !=matriz_ventas:
    print("la matriz original no ha cambiado")
    for i in range(4):
        for j in range(5):
            matriz_copia [i][j] = matriz_copia [i][j] * 0.85
            print(matriz_copia[i][j])
            print("/n")


# Calcular diferencia total en ingresos
diferencia_total = 0

# Verificar si las matrices son diferentes
if matriz_copia != matriz_ventas:
    for i in range(4):  # Asumiendo que la matriz tiene 4 filas
        print("\n")  # Imprime salto de línea
        for j in range(5):  # Asumiendo que cada fila tiene 5 columnas
            diferencia_total += matriz_ventas[i][j] - matriz_copia[i][j]
            print(f"Diferencia acumulada en posición [{i}][{j}]: {diferencia_total}")

    print("\nLa diferencia total en ingresos debido al descuento es:", diferencia_total)
            
            

productos = ["papas", "cebollas", "apio", "zanahorias", "lechuga"]

# Usar comprensión de listas para crear una nueva lista con nombres en mayúsculas
productos_mayusculas = [producto.upper() for producto in productos]

# Mostrar el resultado
print(productos_mayusculas)