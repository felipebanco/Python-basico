#Main sirve para trabajar con todas las clases, instanciar los objetos y operar con los metodos

#Método para importar todo por el asterisco.
from Calculadora import *

#Intanciar el objeto y trabajar con el Método constructor
calculadora1 = Calculadora(5,2)

#Se puede trabajar con todos los métodos, con uno o con ninguno

print(f"La suma es: {calculadora1.sumar()}")
print(f"La resta es: {calculadora1.restar()}")
print(f"La multiplicación es: {calculadora1.multiplicacion()}")
print(f"La división es: {calculadora1.division()}")

#En el caso de potencia se puede trabajar con un solo argumento
print(f"La potencia es: {calculadora1.potencia()}")
