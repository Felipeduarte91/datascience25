#Reto 1: Gestión Avanzada de Tienda (Equipo 1)
#Enunciado del Problema: Diseña un sistema para gestionar un inventario de una tienda con productos clasificados por categorías. El sistema debe permitir agregar productos  con precio, cantidad y categoría, generar reportes ordenados alfabéticamente, calcular el valor total por categoría y eliminar productos con cantidades por debajo de un umbral. Usa un diccionario para el inventario, un conjunto para categorías únicas y bucles while para validaciones y procesamiento.
#Entradas Esperadas:
#• Opción del submenú (1-5).
#• Para agregar: Nombre del producto (texto, mínimo 1 carácter), precio (número decimal mayor a 0), cantidad (entero no negativo), categoría (texto, mínimo 1 carácter).
#• Para calcular: Categoría (texto).
#• Para eliminar: Umbral de cantidad mínima (entero no negativo).
#Salidas Esperadas:
#• Agregar: Mensaje confirmando que el producto se agregó, incluyendo su categoría.
#• Listar: Reporte de todos los productos ordenados alfabéticamente, mostrando nombre,
#categoría, precio y cantidad.
#• Calcular: Valor total de los productos en la categoría especificada, en formato monetario.
#• Eliminar: Lista de productos eliminados por tener cantidades por debajo del umbral, o mensaje indicando que no se eliminaron productos.

inventario = []
productos = []
submenu = "" #opcion del submenu

while submenu != "5":
  print("Menu")
  print("1.Agregar producto")
  print("2.Lista de productos")
  print("3.Calcular el valor total por categoria")
  print("4.Eliminar productos con cantidades por debajo de un umbral") 
  print("5.Salir")
  submenu = input("Ingrese una opcion: ")
  if submenu == "1":
    nombre =input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))
    categoria = input("Categoria del producto: ")
    inventario = int(input(nombre, precio, cantidad, categoria)) # type: ignore
    print("Producto agregado correctamente")
    print("Nombre del producto: ", nombre)
    print("Precio del producto: ", precio)
    print("Cantidad del producto: ", cantidad)
    print("Categoria del producto: ", categoria)
    break
  elif submenu == "2":
      print("Lista de productos: ", inventario)
      break
  elif submenu == "3": 
      print("Valor total por categoria: ", inventario)
      break
  elif submenu == "4":
      print("Producto eliminado por tener cantidad menor al umbral")
      break
      print("Saliendo del programa.....")
      break