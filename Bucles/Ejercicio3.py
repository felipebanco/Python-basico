#Ejercicio 3
'''
Pide numeros y metelos en una lista, cuando el usuario meta un 0 ya dejemos de insertar.
Por ultimo, muestra los numeros ordenados de menor a mayor.
'''

numero = int(input("Digite un numero"))
lista=[]

while numero != 0:
    lista.append(numero)
    numero = int(input("Vuelva ingresar otro numero: "))

lista.sort()
print(lista)