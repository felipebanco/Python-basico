#Pilas

'''Tipo de estructura donde un valor es el ultimo en entrar y el primero en salir'''

pila = [1,2,3] #Se trabajan como listas

pila.append(4) #Se agregan elementos al fila de la pila
pila.append(5)

print(pila)

n = pila.pop() #Saca o elimina el ultimo elemento de la pila, y se guarda en una variale n.

print(f"Eliminando el elemento {n}")
print(pila)