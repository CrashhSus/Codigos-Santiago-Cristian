from funciones import sumar, restar

def mostrar_menu():
    print("Calculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-3): ")

    if opcion == "3":
        print("bye bye")
        break

    if opcion not in {"1", "2"}:
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

    print(f"Resultado: {resultado}\n")
