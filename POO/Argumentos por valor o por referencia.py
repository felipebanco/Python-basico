#Argumentos por valor o por referencia
'''
#Cuando un argumento es por valor, la funcion recibe una copia del valor original.
#Cuando el argumento es por referencia, la funcion recibe el valor original para ser modificado,
todos los tipos de colecciones (listas, tuplas, diccionarios etc.), se pasan por referencia.
Todos los datos en python se pasan por argumento por valor a excepcion de las colecciones, cualquier
modificacion a la funcion de un valor por referencia afecta direcatamente al valor original.
'''

#Argumentos por valor
def doblar_numero(numero):
    numero *= 2
n = 5
doblar_numero(n)
print(n)
print()

def doblar_numero1(numero):
    return numero*2
numero = 5
numero = doblar_numero1(numero)
print(numero)
print()


#Argumentos por referencia
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
n = [5,10,15,20]
doblar_valores(n)
print(n)
print()

def doblar_valores1(numeros):
    for i, n in enumerate(numeros):
        numeros[i]*=2
n = [5,10,15,20]
doblar_valores1(n[:]) #Pasar un argumento por referencia a argumento por valor, una copia de las coleccion
print(n)