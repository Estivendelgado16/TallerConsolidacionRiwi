frutas = ["Apple","Orange","Strawberry"]

while True:
    try:
        print("\n LISTA DE FRUTAS\n \n 1. Agregar\n 2. Eliminar\n 3. Salir")
        opcion = int(input("\n digita la opcion: "))
    except ValueError:
        print("\nERROR: ingresa un numero")
        continue

    if opcion == 1:
        frutNuev = input("Ingresa una fruta: ")
        if frutNuev == "" or " ":
            print("ERROR: intentalo de nuevo")
        else: 
            frutas.append(frutNuev.title().strip())
            print(f"\nlista de prodctos{frutas}")
    elif opcion == 2:
        print(frutas)
        elimFruta = input("digita la fruta que desea eliminar: ")

        if elimFruta == "" or " ":
            print("ERROR: intentalo de nuevo")
        else: 
            frutas.remove(elimFruta.title().strip())
            print(frutas)
    else:
        print("saliendo")
        break


