<<<<<<< HEAD
<<<<<<< HEAD
from funciones import multiplicacion, division
def mostrar_menu():
    print("Seleccione una operación:")
    print("4. Multiplicación")
    print("5. División")
    print("6. Salir")
    opcion = input("Ingrese su opción: ")
    return opcion
def ejecutar_operacion(opcion, a, b):
    if opcion == '4':
        resultado = multiplicacion(a, b)
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == '5':
        resultado = division(a, b)
        print(f"El resultado de la división es: {resultado}")
    elif opcion == '6':
        print("Saliendo del programa.")

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == '6':
            ejecutar_operacion(opcion, 0, 0)
            break
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            ejecutar_operacion(opcion, a, b)
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese números válidos.")
=======
from funciones import sumar, restar
=======
from funciones import sumar, restar, multiplicacion, division
>>>>>>> Santiago

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
<<<<<<< HEAD
        resultado = restar(num1, num2)

    print(f"Resultado: {resultado}\n")
>>>>>>> 59f3fc742e8891305e10ba5b78311dbf55cd9730
=======
        resultado = restar(num1, num2)
>>>>>>> Santiago
