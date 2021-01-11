#Listas o Colecciones
'''
Dato estructurado flexible en el que se pueden almacenar todo tipo de datos
desde booleanos, caracteres, float, int, cadenas ect.
Los valores de una lista se alcenan entre [] y se separan con comas.
'''

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"] #Dias laborales de la semana
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", 34, True, [0,1,2,3]]
lista3 = [1,2,3,4,5,6]
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9]
lista4 = [1, 2, 3, 4, 5, 'Hola', 1, 2, 3, 4, 5]
lista5= [8,9,1,6]
lista6= [6,1,9,8]
lista7= lista5,lista6
print(lista) #Se imprime toda la lista
print(lista[2]) #Si se escribe un sub indice de la lista solo se imprime dicho elemento
print(lista[-3])#Si se escribe en negativo el sub indice se imprime del principio hasta el fin
print(lista3[0:3])#Se imprime desde 0 hasta la posicion especificada
print(len(lista))#Funcion que cuenta la cantidad de elementos de las lista
print('Felipe'in lista1) #Sirve para buscar elementos en las listas
print(lista1.index(5)) #Muestra por pantalla el sub indice de dicho elemento
print(lista1)
lista3= lista1+lista2 #Suma de elementos de las listas
print(lista3)
print(lista4.count(3)) #Funcion que cuenta cuantas veces aparece dicho valor en la lista
#lista.sort() ordena de mayor a menor


lista1.append(6) #Funcion que agrega elementos a la lista
lista1.append("Felipe")
lista1.insert(2,3)#Funcion que agrega elementos en una posicion especifica de la lista
#Primero se escribe el indice separado por una coma junto con el elemento que se quiere agregar.
lista1.extend([6,7,8])#Funcion que agrega mas de un elemento al final de la lista
lista1.pop(3)#Elimina elementos de cierta pocision de la lista
lista4.remove(5)#elimina elementos de la lista sin necesidad de especificar el indice
lista2.clear() #Borrar todos los elementos de la lista
print(lista1)
print(lista4)
print(lista2)
print(lista7)


