from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("Calculadora open source")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Divicion")
    print("5. Suma avanzada (mas de dos números)")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado es: {sumar(num1, num2)}")
        elif opcion == "2":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado es: {restar(num1, num2)}")
        elif opcion == "3":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado es: {multiplicar(num1, num2)}")
        elif opcion == "4":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            if num2 != 0:
                print(f"El resultado es: {dividir(num1, num2)}")
            else:
                print("Error: No se puede dividir entre 0.")
        elif opcion == "5":
            cantidad = int(input("¿Cuántos números deseas sumar?: "))
            numeros = []
            for i in range(cantidad):
                numero = float(input(f"Introduce el número {i+1}: "))
                numeros.append(numero)
            print(f"El resultado de la suma avanzada es: {suma_avanzada(numeros)}")
        elif opcion == "6":
            print("Gracias por usar la calculadora. ¡Adiós!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()

