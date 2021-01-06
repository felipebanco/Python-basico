#Funciones Recursivas
#Ejercicio 5
'''
Desarrollar un programa que permite sumar los dígitos de un número con ayuda de una función recursiva
Ej: Entrada 126
    Salida: 6
'''

def sumarDigitos(num):
    if num == 0: #Caso Base
        resultado = 0
    else: #Caso Recursivo
        resultado = sumarDigitos(int(num/10)) + (num%10)
    return resultado
valor = sumarDigitos(123)
print(valor)


lista = [1,2,3,4,67]

def sumar(lista): #Método tradicional sumar elementos de una lista
    suma = 0
    for elemento in  lista:
        suma += elemento
    return suma
print(sumar(lista))

'''
Método desglosado

lista = [1,2,3,4,5]

suma = 1 + [2, 3, 4, 5]
            2 + [3, 4, 5]
                3 + [4, 5]
                    4 + [5]
                        5 + []

'''

lista1 = [23,45,67,78,34]

def sumar(lista1): #Método con función recursiva sumar elementos de una lista
    if lista1 == []:
        suma = 0
    else:
        suma = lista1[0] + sumar(lista1[1:]) #Suma el primer elemento con los restantes
        '''       23      +     [45,67,78,34]'''
    return suma
print(sumar(lista1))

