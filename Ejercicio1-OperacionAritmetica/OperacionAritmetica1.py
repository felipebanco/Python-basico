# Elementos Básicos

'''
1. Escribir la siguiente expresión en expresión Algoritmica.
'''

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
operacion = 0

operacion = (a**3 * (b**2-2*a*c))/(2*b)
resultado = round(operacion)
print(f"El resultado total de la operación es: {resultado}")