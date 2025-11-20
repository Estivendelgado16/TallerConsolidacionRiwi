while True:
    try:
        edadAct = int(input("Ingresa tu edad actual: "))
        edadFut = int(input("Ingresa los años que deseas calcular: "))

        total = edadAct + edadFut 
        print(f"En {edadFut} años, tendra {total} años")
        
    except ValueError:
        print("Error: ingresa datos validos")

        