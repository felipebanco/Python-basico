
i = 0
suma = 0
promedio = 0

numeros = int(input("Ingrese la cantidad de numeros a sumar: "))

while (i < numeros):
    nro = int(input("Ingrese un numero: "))
    suma = suma + nro
    i=i+1
promedio = suma / numeros
print(f"El promedio es {promedio}")