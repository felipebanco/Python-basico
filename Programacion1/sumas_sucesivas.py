'''Realice un algoritmo para la multiplicación mediante sumas sucesivas de A*B
    Ejemplo: 3*4 = 3+3+3+3 = 81'''


a = int(input("Ingrese un valor: "))
b = int(input("ingrese otro valor: "))



for a in range(a,b):
    a*=b
    

print(a)