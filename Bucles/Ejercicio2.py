#Ejercicio 2
'''
Llenar una lista con numero del 1 al 10, luego modificar los elemnetos de la lista multiplicandolos
por un numero que el usuario digite.
'''

lista = list(range(1,11))

print("Lista Original")
for i in lista:
    print(i, end="-")

valor= int(input("\nDigite el numero que desea multiplicar: "))

for indice, i in enumerate(lista):
    lista[indice]*=valor

print(f"\nLista final de los elementos multiplicados por: {valor}")
for i in lista:
    print(i, end="-")
