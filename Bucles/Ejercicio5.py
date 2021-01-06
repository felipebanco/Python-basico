#Ejercicio 5
'''Hacer un programa que calcule el factorial de un numero'''

numero = int(input("Ingrese el numero que desea calcular su factorial: "))
factorial = 1

if numero < 0:
    print(f"No se puede calcular el factorial del numero {numero}")
elif numero == 0:
    print("No se puede calcular el factorial de 0.")
else:
    for i in range(1, numero+1, 1):
        factorial *= i

    print(f"El factorial del numero ingresado es: {factorial}")
