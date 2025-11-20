while True:
    try:
        edad = int(input("Ingrese edad: "))

        if edad <= 0:
            print("Error: ingresa numeros positivos")
        elif edad < 18:
            print("Eres menor de edad, paso restringido")
            break
        else: 
            print("eres mayor de edad, bienvenido")
            break
    except ValueError:
        
        print("Error: ingrese un valor valido")



    
