print("Haz una suma")

while True:
    try:
        num1 = float(input("Por favor ingresa un número: "))
        num2 = float(input("Por favor ingresa el segundo número: "))

        resultado = num1 + num2
        print(f"✅ El resultado es: {resultado}")
        
        break  

    except ValueError:
        
        print("Error: debes ingresar solo números (usa punto para decimales). Intenta de nuevo.\n")




    
