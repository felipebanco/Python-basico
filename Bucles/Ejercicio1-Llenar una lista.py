#Ejercicio 1 - Llenar una lista con numero del 1 al 50 y mostrarlos en fila

lista=[]
i=1

#Agregando numeros a la lista
while i<=50:
    lista.append(i)
    i+=1

#Mostrando por pantalla los numeros en fila
for i in lista:
    print(i, end="-")
