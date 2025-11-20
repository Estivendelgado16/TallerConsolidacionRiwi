#Sumar hasta que el usuario escriba 0


cont = 0

while True:

    num = float(input("Ingresa un numero: "))

    if num != 0:
        cont += num
        print(cont)
    else: 
        print("cero")
        break
    

    

    