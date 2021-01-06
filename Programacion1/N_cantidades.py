'''Se requiere un algoritmo para determianr de N cantidades, cuántas son menores o iguales
a 0, y cuantas mayores a 0. '''

cantidades = 0
lista = []
menoresA_cero = 0
mayoresA_cero = 0

print('Bienvenido, a continuación detalle cuantos números deseas procesar')
cantidades = int(input('Ingresa el valor: '))

for i in range(cantidades):
    valores = int(input("Ingrese los números: "))
    lista.append(valores)

for x in lista:
    if x <= 0:
        menoresA_cero+=1
    elif x > 0:
        mayoresA_cero+=1
print("Existen ",menoresA_cero, "cantidades menores o iguales a 0")
print("Existen ",mayoresA_cero, "cantidades mayores a 0")


