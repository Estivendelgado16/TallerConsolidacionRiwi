def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por 0"
    return a / b

while True:
    print("\n CALCULADORA")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Ingresa un número válido.")
        continue

    if opcion == 5:
        print("Saliendo del programa...")
        break

    if opcion not in (1, 2, 3, 4):
        print("Opción no válida.")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Debes ingresar números válidos.")
        continue

    operaciones = {
        1: sumar,
        2: restar,
        3: multiplicar,
        4: division
    }

    resultado = operaciones[opcion](num1, num2)
    print(f"El resultado es: {resultado}")
