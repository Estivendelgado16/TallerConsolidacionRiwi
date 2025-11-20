while True:

    try:

        num = float(input("Ingresa un numero: "))

        if num < 0:
            print("El numero es negativo")
            break
        elif num == 0:
            print("El numero es igual a cero")
            break
        else:
            print("El numero es positivo")
            break
            
    except ValueError:
        print("Error: ingresa un dato valido")
        