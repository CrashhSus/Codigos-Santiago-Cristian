<<<<<<< HEAD
=======
from funciones import sumar, restar, multiplicacion, division

def mostrar_menu():
    print("Calculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("bye bye")
        break

    if opcion not in {"1", "2", "3", "4"}:
        print("El número no está en la lista\n")
        continue

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Entrada inválida. Debes ingresar números.\n")
        continue

    if opcion == "1":
        resultado = sumar(num1, num2)
    elif opcion == "2":
        resultado = restar(num1, num2)
        
>>>>>>> Santiago

<<<<<<< HEAD
=======
    if opcion == "3":
        resultado = multiplicacion(num1, num2)
    elif opcion == "4":
        resultado = division(num1, num2)

    print(f"Resultado: {resultado}\n")
>>>>>>> cristian