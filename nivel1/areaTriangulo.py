while True:
    try:
        base = int(input("ingresa la base del triangulo: "))
        alto = int(input("ingresa la altura del triangulo: "))
        

        resultado = (alto * base) / 2
        print(f"el area del triangulo es: {resultado}")
        break
    except ValueError:
        print("error: ingresa datos validos")

        




