#Ejercicio 2
'''
Hacer un programa que pida el ancho y alto de un rectángulo y con la ayuda de la funcion lo dibuje con *
'''

def dibujar_rectangulo(ancho,alto):
    for i in range(alto): #Bucle for anidado
        for j in range(ancho):
            print("*", end="") #Se imprimen de manera consecutiva sin hacer un salto de linea
        print() #Salto de linea para dibujar el rectangulo, recorriendo el primer bucle

ancho = int(input("Ingrese el ancho del rectangulo: "))
alto = int(input("Ingrese el alto del rectangulo: "))
print()
dibujar_rectangulo(ancho,alto)
