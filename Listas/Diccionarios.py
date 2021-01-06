#Diccionarios
'''tipo de colección donde los elementos tambien se guardaan desordenados con 2 elementos
Por posicion la clave y el valor. No pueden haber claves duplicadas.'''


diccionario = {"Azul":"Blue","Rojo":"Red","Verde":"Green"}
#Primero la clave y despues separado por dos punto el valor.

diccionario ["Amarillo"]= "Yellow"
#Agregando elementos al diccionario, especificando su valor.

del(diccionario["Verde"])
#Elimiando un elemento del diccionario.

diccionario2 = {"Felipe": [19, 1.80]}
#Diccionario con una lista en su interior.

diccionario3 = {"Lucas": {"Edad":19, "Ciudad": "Mendoza"}}
#Diccionario con un diccionario en su interior como valor a las claves.

print(diccionario)
print(diccionario["Azul"]) #Especificando la clave obtengo su valor ej: blue
print(diccionario2)
print(diccionario3)