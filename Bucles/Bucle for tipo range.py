#Bucle for tipo range

'''
Bucle especializado en repetir un ciclo con un numero elevado de repeticiones
'''

for i in range(20):
    print(i)

for i in range(5,11):
    print(i)

for i in range(2,21,2): #El ultimo numero representa el paso que recorre, de dos en dos.
    print(i)

# Para iterar sobre los índices de una secuencia se puede combinar range() y len() 
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
