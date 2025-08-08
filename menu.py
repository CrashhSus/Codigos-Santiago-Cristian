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