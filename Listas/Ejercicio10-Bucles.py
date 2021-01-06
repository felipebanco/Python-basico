#Ejercicio 10
'''Hacer un programa que pida por teclado una cadena, luego meter los caracteres en una lista
sin repetir caracteres.'''

cadena = input("Ingrese o escriba una frase o cadena: ")
lista = []

for i in cadena:
    if i not in lista: #Si los caracteres de la cadena no estan en la lista, éstos se van agregando.
        lista.append(i)
print(f"\nLista de caracteres sin repetir {lista}")