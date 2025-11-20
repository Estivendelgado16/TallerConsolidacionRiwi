while True:

    try:
        num = int(input("Ingresa el numero: "))
    except ValueError:
        print("Error: ingresa un numero")
        continue


    if num % 2 == 0:
        print("es par")
        break
    else:
        print("es impar")
        break