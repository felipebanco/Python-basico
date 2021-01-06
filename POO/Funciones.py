#Algoritmo de prueba de funciones.

'''La funciones en python se incializan en "Def"

factorial_numero() #Con esta linea de codigo estoy mandando a ejecutar la funcion
factorial_numero()
factorial_numero()'''

def factorial_numero():
    numero = 5
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
        print(factorial)

factorial_numero()
factorial_numero()
'''Si se quiere volver a repetir la funcion solo basta con copiar y pega N veces la ultima
linea de codigo de la funcion que es la que se imprime por pantalla'''

