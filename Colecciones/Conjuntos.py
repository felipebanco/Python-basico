#Conjuntos
'''
Tipo de coleccion donde los elementos se agregan o se encuentran de forma desordenada.
Su principal caracteristica es que no pueden haber elementos duplicados.
Para definir un conjunto se tiene que escribir la funcion "set" para diferenciarlos de los diccionarios
y si queremos crearlos vacios.
Se escriben entre {}.
No soportan otro tipo de colecciones.
'''
conjunto=set()
conjunto= {1, 2, 3, "Hola", 4.56}
conjunto.add(5) #Funcion que permite agregar un valor al conjunto.
conjunto.add("Adios")
conjunto.add("a")
conjunto.discard(1)#Funcion que permite eliminar un elemento de la coleccion.
#conjunto.clear() Funcion que borra todos los elementos del conjunto

print(3 in conjunto)#Buscar un elemnto en el conjunto
print(conjunto)