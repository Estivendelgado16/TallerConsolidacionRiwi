import random

numran = random.randint(1,10)
while True:

    try:
        num = int(input("\nAdivina el numero\n Ingresa un numero del 0 al 9: "))
    except ValueError:
        print("\nError solo numeros")
        continue

    if num == numran:
        print(f"\nAdivinaste el numero: {numran}")
        break 
    else:
        print("\nvuelve a intentar")

    