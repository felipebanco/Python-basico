#Tuplas
'''
Tipo de coleccion donde no se pueden modificar los datos.
Se usan parentesis en vez de corchetes.
Soporta diferentes tipos de datos igual que las listas incliso tambien se pueden escribir
lista dentro de la tupla.
'''
tuple = (4, 'Hola', 4.79, True, False, [1,2,3,4,5], 4)

print(tuple)
print(tuple[1]) #Se pueden mostrar valores especificos de la tupla aclarando su indice.
print(tuple[-1]) #Tambien se pueden usar indices en negativo del fin al principio.
print(4 in tuple) #Se puede si existe o no un determinado valor en la tupla.
print(tuple.index('Hola'))#Se pueden buscar valores especificando su indice.
print(tuple.count(4)) #Contador de cuantas veces figura dicho valor en la tupla.
print(len(tuple)) #Indica cuantos elemntos en total tiene esta tupla.
lista=list(tuple) #Transformar la tupla en una lista
print(lista)

'''Tambien se puede transformar una lista en tupla
lista=[1,2,3,4,5]
tupla=tuple(lista)
print(tupla)'''

