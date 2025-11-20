#Números pares: guardar solo los pares.
listPares  = []


while True:

    print("Que opcion desea --\n 1.saber que numero es par \n 2.salir\n ")
    opcion = input(":")

    if opcion == "2":
        print("Saliendo. . .")
        break

    elif opcion == "1":
        num = input("ingresa un numero (o enter para salir):")

        if num.strip() == "":
            print("saliendo de la opcion 1. . .")
            break
        

        try:
            num = float(num)

        except ValueError:
            print("no es unn numero valido")
            continue

        if num % 2 == 0:
            print("El numero es par")
            listPares.append(num)
            print(listPares)
        else:
            print("El numero es impar")
        
            
    else: 
        print("opcion no valida")
        