#Funciones Recursivas
'''
funciones iterativas que en algun momento finalizan, se llaman dentro de la misma funcion
'''
#Ejercicio 4:
'''
Desarrollar un programa para calcular el factorial de un numero con ayuda de una funcion recursiva
'''

def factorial(num):
    print(num)
    if num>0:
        resultado=num*factorial(num-1)
    else:
        resultado=1

    return resultado

valor = factorial(5)
print(f"El resultado del factorial de 5 es {valor}")