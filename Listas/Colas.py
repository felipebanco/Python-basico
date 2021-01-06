#Colas

'''Tipo de estructura donde un valor es el primero en entrar y el primero en salir'''

colas = ["Maria", "Alejandro", "Jose", "Mario"]

colas.append("Carla")
print(colas)
#Agregando elementos al final y mostrando por pantalla

n = colas.pop(0) #Sacando el primer elemento en el subindice 0
print(f"La primera en salir es {n}")
print(colas) #Personas restantes en la cola
