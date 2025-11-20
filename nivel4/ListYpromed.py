#Lista de números y promedio.

ListNum = []

while True:
    print("Digita enter  para finalizar")
    
    num = input("Ingresa las notas: ")

    if num:
        num = float(num)
        ListNum.append(num)
    else:
        promedio = sum(ListNum) / len(ListNum)
        print(f"El promedio es: {promedio}")
        break


        



