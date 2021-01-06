#Diccionarios Parte 2

equipo = {10:"Paulo Dybala", 11: "Douglas Costa", 7: "Cristiano Ronaldo", 17: "Mario Mandzukic"}

print(equipo)

print(equipo.get(7, "No existe ese jugador")) #Se especifica una clave que puede o no existir y si no existe
#Se muestra por pantalla un pequeño mensaje.

print(10 in equipo) #Metodo para buscar si un elemento se encuntra en dicho diccionario. True or False.

print(equipo.keys()) #Imprimir solo las claves.

print(equipo.values()) #Imprimir todos los valores.

print(len(equipo)) #Metodo para mostrar cuantos jugadores hay en un equipo.

#equipo.clear() #Metodo para limpiar todo el diccionario.
#print(equipo)