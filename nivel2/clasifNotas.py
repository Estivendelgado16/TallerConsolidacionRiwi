#Clasificador de notas (Excelente, Aprobado, Reprobado).

while True:

    try:
        nota = float(input("Ingresa tu nota: "))
    except ValueError:
        print("Ingresa numeros")
        continue


    if nota <= 65:
        print("reprobado")
        break
    elif 65 < nota <= 80:
        print("aprobado")
        break
    else:
        print("Excelente")
        break
        