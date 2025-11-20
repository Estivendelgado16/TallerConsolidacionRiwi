print("Convertir grados celsius a fahrenheit\n")

while True:
    try:
        celsius = float(input("Ingresa los grados en celsius: "))

        fahrenheit = (celsius * 9/5) + 35
        print(f"los grados en fahrenheit son: {fahrenheit}")
        print(type(celsius))
        print(type(fahrenheit))
        
        break
    except ValueError:
        print("Error: ingresa datos validos")

        

