#Ejercicio 4

'''Construir una calculadora que pueda realizar las 4 operaciones basicas.
 El usuario debe especificar la operación con el primer caracter del nombre
 de la operacion'''

letra=input("Digite la primera letra de la operacion que desea realizar: ")
suma=0
resta=0
multiplicacion=0
division=0

if letra =='S' or letra =='s':
    num1 = float(input("\nDigite un numero: "))
    num2 = float(input("\nDigite otro numero: "))
    suma = num1+num2
    print(f"\nEl resultado de la suma es {suma:.2f}")
elif letra =='R' or letra =='r':
    num1 = float(input("\nDigite un numero: "))
    num2 = float(input("\nDigite otro numero: "))
    resta = num1 - num2
    print(f"\nEl resultado de la resta es {resta:.2f}")
elif letra =='P' or letra =='p' or letra =='M' or letra =='m':
    num1 = float(input("\nDigite un numero: "))
    num2 = float(input("\nDigite un numero: "))
    multiplicacion = num1 * num2
    print(f"\nEl resultado de la multiplicacion es {multiplicacion:.2f}")
elif letra == 'D' or letra == 'd':
    num1 = float(input("\nDigite un numero: "))
    num2 = float(input("\nDigite un numero: "))
    division = num1 / num2
    print(f"\nEl resultado de la division es {division:.2f}")
else:
    print("La letra seleccionada no coincide con ninguna de las operaciones.r")

print("\nFin del programa")