"Calcular la raiz cuadrada"

from math import * #Importa todas las librerias y funciones matematicas
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
resultado = 0


resultado = sqrt(a*a+b*b)
resultado_final = round(resultado)

print(f"El resultado del calculo es: {resultado_final}")