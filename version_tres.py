print("¿Qué quieres hacer?")
print("1. Sumar")
print("2. Restar")
print("3. Dividir")

opcion = input("Elige (1, 2 o 3): ")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if opcion == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif opcion == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif opcion == "3":
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = num1 / num2
        print("Resultado:", resultado)

else:
    print("Opción no válida")
