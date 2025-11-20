while True: 
    print("Comparador de tres números: mayor y menor")

    try:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        num3 = float(input("Ingresa el segundo numero: "))
    except ValueError:
        print("Error: ingresa numeros")
        continue

    if num1 > num2 and num1 > num3:
        print(f"El numero mayor es: {num1}")
    if num1 < num2 and num2 > num3:
        print(f"El numero mayor es: {num2}")
    if num3 > num1 and num3 > num2:
        print(f"El numero mayor es: {num3}")
    
    if num1 < num2 and num1 < num3:
        print(f"El numero menor es: {num1}")
    if num2 < num1 and num2 < num3:
        print(f"El numero menor es: {num2}")
    else:
        print(f"El numero menor es: {num3}")
        break


