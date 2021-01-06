#Repaso

for i in range (1,3,1): #Llega hasta el numero 2 y lo multiplica por 2
    print(i*2)

for i in range(-1,-4,-1): #Retrocede de 1 en 1 hasta el numero 3
    print(i)

for i in range(5):
    if (i % 2) == 0:
        print(i)


vocales = ["a","e","i","o","u"]
texto = "Programación primero"
print(texto.count("p"))
'''
Ejercicio
total = texto.count("p")
la funcion count cuenta la cantidad de veces que aparece un elemento en la lista, pero solo funciona
con la palabra reservada print
'''

i = 1
n = 3
suma = 10
while i < n:
    suma = suma + i
    i = i + 1
print(suma)

i = 1
n = 5
suma = 0
while i <= n:
    if i == 3:
        break
    else:
        suma = suma + i # 1
    i = i + 1           # 3
print(suma)  # 3

lista1 = [1,2,3,4]
print(lista1[0:3])

lista2 = [0,1,2]
for v in range(2):
    lista2.insert(0,lista2[v+1])
print(lista2)
