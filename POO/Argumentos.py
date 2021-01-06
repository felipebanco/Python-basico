#Funciones con Argumentos, Programación Orientada a Objetos

'''Calcular un factorial de un numero n
'''

def factorial_numero(numero):
    factorial = 1
    while numero > 0:
        factorial *= numero
        numero -= 1
        print(factorial)
    
    return factorial

# print(f"El factorial es: {factorial_numero(4)}")
print(f"El factorial es: {factorial_numero(5)}")
# print(f"El factorial es: {factorial_numero(6)}")
