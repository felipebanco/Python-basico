'''
import random

arreglo = []
arreglo_inverso = []

for i in range(0,10,1):
    n = random.randint(1,15)
    arreglo.append(n)
    longitud_arreglo = len(arreglo)

print(arreglo)

for item in reversed(arreglo):
    arreglo_inverso.append(item)


print(arreglo_inverso)
'''

import random

arreglo = []
def generar_arreglo(arreglo):
    for i in range(0,10,1):
        n = random.randint(1,15)
        arreglo.append(n)
        longitud_arreglo = len(arreglo)
    return arreglo

devolver_arreglo = generar_arreglo(arreglo)
print(devolver_arreglo)

arreglo_inverso = []
def mostrar_inverso(arreglo_inverso):
    for item in reversed(arreglo):
        arreglo_inverso.append(item)
    return arreglo_inverso

print(mostrar_inverso(arreglo_inverso))