#Reto 1: Gestor de Números Pares e Impares
#Crea un programa que tenga un menú interactivo usando un ciclo while. El usuario podrá:
 #- Agregar un número a una lista
 #- Ver la lista completa
 #- Ver solo los números pares
 #- Ver solo los números impares
 #- Salir del programa

numeros = 0 
opcion = ""
sumador = 0

while opcion != "5":
    print("Menu")
    print("1.Agregar un numero")
    print("2.Ver la lista completa")
    print("3..Ver solo los numeros pares")
    print("4.Ver solo los numeros impares")
    print("5.Salir")
    
    opcion =input("Ingrese una opcion: ")
    if opcion == "1":
        numeros =int(input("Ingrese un numero: "))
        print("Numero ingresado correctamente")
        print("Numero ingresados: ")
        if numeros %2 == 0:
            print("El numero es par")
            print("Numeros pares: ", numeros)
        else:
            print("El numero es impar")
            print("Numeros impares: ", numeros)
            break
            print("Saliendo del programa.....")
            break

            print("Opcion no válida")

            print("Saliendo del programa")
           
            print("Saliendo del programa....")
            
if opcion == "2":
  print("Lista completa de los numeros: ", numeros) 
print(numeros)
if opcion == "3": #ver solo los numeros pares
  print("Numeros pares: ", numeros)
if numeros %2 ==0:
        print(numeros)
if opcion == "4": #ver solo numeros impares
  print("Numeros impares: ", numeros)
if numeros %2 !=0:
        print(numeros)
        print("Saliendo del programa....")
else:
    if opcion == "5": 
#Salir del programa
      print("Saliendo del programa....") 