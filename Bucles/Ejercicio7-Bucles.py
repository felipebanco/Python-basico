#Ejercicio 7 - Juego adivina un número.
'''Realizar un juego para adivinar un numero. Para ello generar un numero aleatorio entre 0-100,
luego ir pidiendo números indicando "es mayor" o "es menor" según sea mayor o menor respecto a N.
El proceso termina cuando el usuario acierta y mostrar el número de intentos.'''

import random
#Modulo que permite generar un numero entero dentro de un rango especificado.
aleatorio = random.randint(0,100)

print("\tBienvenido al juego adivina el numero.")

iterador = 0 #Contador de repeticiones

while True: #Bucle infinito de iteraciones
    numero = int(input("\tIngrese un numero para jugar: "))
    iterador += 1 #El usuario va jugando se va sumando de 1 en 1 la cantidad de numeros que ingresa.
    if numero>aleatorio:
        print("\tNo es el numero, ingresa un numero menor")
    elif numero<aleatorio:
        print("\tNo es el numero, ingresa un numero mayor")
    else:
        print(f"\tFelicidades acabas de adivinar el numero: {aleatorio}")
        break #Finaliza la ejecucion del bucle.
print(f"\tSu numero de intentos es: {iterador}.")