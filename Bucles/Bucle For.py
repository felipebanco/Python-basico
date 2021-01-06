#Bucle For
'''
Tipo de bucle en que se va a repetir una cierta cantidad de veces una sentencia, es finito
'''

coleccion=[5,6,7,8]
coleccion1={"Alejandro":12,"Felipe":19} #diccionario

for i in coleccion1:
    print(f"{coleccion1[i]}") #imprime los valores numericos de la coleccion

for i in coleccion1:
    print(f"{i} -> {coleccion1[i]}") #imprime clave y valor numerico

for i in coleccion:
    print(coleccion)

for i in [1,2,3]:
    print("Hola")

for i in [2,3,4,"Felipe"]:
    print(i)