#Ejercicio 4
'''Hacer un programa para ingresar el radio de un círuclo y se reporte su area
y la longitud de su circunferencia.'''

import math #El modulo "math" importa muchas funciones matematicas entre ellas el valor de Pi
radio = float(input("Ingrese el radio de la circunferencia: "))


area = math.pi*radio**2 #Math.pi equivale a escribir 3.14
longitud = 2*math.pi*radio

print(f"El area total del circulo es: {area:.2f}")
print(f"La longitud total del circulo es: {longitud:.2f}")

'''Escribir la variable solicitada mas dos puntos, un punto, un numero y la letra f
estamos redondeando el el valor de variable para que solo nos muestre 2 decimales
despues de la coma, la funcion es similar a escribir resultado=round(variable)'''