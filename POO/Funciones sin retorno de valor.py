#Funciones
'''Bloque de codigo dentro de un programa que permiten resolver un problema especifico
se puede reutilizar el codigo cuantas veces queramos. Existen dos tipos de funciones en Python:
 -Funciones con retorno de valor.
 -Funciones sin retorno de valor.
Las funciones deben llevar el nombre de la accion que van a realizar'''
#Funciones sin retorno de valor

def saludar(): #En los parentesis se escriben los parametros que se quieran utlizar.
    print("Hola amigo.")
saludar() #Para que la función se ejecute es necesario volverla a llamar separada de la identación.
#Se puede llamar y ejecutar cuantas veces queramos.

def saludar(nombre):
    print(f"Hola {nombre}")
saludar("Agustin.")
saludar("Carlos.")

def tabla_multiplicar(numero): #Se necesita el parametro numero para ejecutar el programa.
    for i in range(1,11): #tabla de multiplicar del 1 al 10.
        print(f"{numero} * {i} = {numero*i}") #Operacion.
tabla_multiplicar(5) #El programa va a recibir el parametro 5 y ejecutar la funcion.
print() #Salto de línea.
tabla_multiplicar(3) #tabla de multplicar del numero 3.