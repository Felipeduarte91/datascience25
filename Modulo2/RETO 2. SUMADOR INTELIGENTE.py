#Reto 4: Sumador Inteligente con Control de Corte
#Haz un programa que permita al usuario ingresar números en un menú:
#- Ingresar un número
#- Ver suma total
#- Ver números ingresados
#- Reiniciar suma
#- Salir (si se ingresa un número negativo, el programa debe avisar y salir automáticamente)

opcion = ""
sumador = ""
numero = ""
while opcion != "5":
    print("Menu")
    print("1.Ingresar un numero")
    print("2.Ver suma total")
    print("3.ver numeros ingresados")
    print("4.Reiniciar suma")
    print("5.Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        numero = int(input("Ingrese un numero: "))
        if numero <= 0:
            print("Numero negativo, saliendo del programa....")
            break
    if opcion == "2":
        sumador = [sumador] + [numero] 
        print("La suma total es: ", sumador)
        break
        if opcion == "3": #ver numeros ingresados
            print("Numeros ingresados: "    , numero)
            break
            if opcion == "4":
                sumador = 0
                print("Suma reiniciada")
                break
                if opcion == "5":
                    print("Saliendo del programa....")
                    break
