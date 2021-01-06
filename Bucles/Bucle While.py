#Bucle While

'''
El ciclo se repite una cantidad determinada o indeterminada de veces mientras se cumpla una condicion,
tambien es posible que el bucle no se ejecute ninguna vez.
'''

numero = int(input("Digite un numero: "))

while numero<0:
    print("Error")
    numero = int(input("Por favor ingrese un numero positivo: "))

print(f"\nLa raiz cuadrada de su numero es: {(math.sqrt(numero)):.2f}") #funcion para raiz cuadrada.
