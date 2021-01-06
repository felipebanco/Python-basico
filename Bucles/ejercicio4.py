#Ejercicio
'''Hacer un programa para sumar numeros pares dentro de un rango.'''

suma=0
a = int(input("Digite el numero de inicio del rango: "))
b = int(input("Digite el numero limite del rango: "))

if a % 2 != 0:
    a += 1

for i in range(a, b+1, 2):
    suma += i

print(f"La suma total de los numeros pares del rango es: {suma}")


