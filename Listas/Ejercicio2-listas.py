#Ejercicio 2

'''Escriba un programa que tenga 2 listas y que a continuacion, cree las siguientes listas
en las que no puede haber repeticiones:
1- Lista de elementos que aprecen en las dos listas.
2- Lista de elementos que aparecen en la primera lista, pero no en la segunda lista.
3- Lista de elementos que aparecen en la segunda lista, pero no en la primera lista.
4- Lista de elementos que aparecen en ambas listas.
'''

lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

#Eliminar los elementos repetidos de ambas listas, tranformandolas en conjuntos
a = set(lista1)
b = set(lista2)

union = list(a | b) #1
soloA = list(a - b) #2
soloB = list(b - a) #3
interseccion = list(a & b)  #4

print(f"\n1-Lista de elementos que aprecen en las dos listas: {union}")
print(f"\n2-Lista de elementos que aparecen en la primera lista, pero no en la segunda lista: {soloA}")
print(f"\n3-Lista de elementos que aparecen en la segunda lista, pero no en la primera lista: {soloB}")
print(f"\n4-Lista de elementos que aparecen en ambas listas: {interseccion}")