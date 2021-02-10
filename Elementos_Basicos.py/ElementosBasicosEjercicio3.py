#Ejercicio 3
'''Hacer un programa que intercambie el valor de dos variables'''

a = input("Ingrese el valor de a->:  ")
b = input("Ingrese el valor de b->: ")


aux = a
a = b
b = aux

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")