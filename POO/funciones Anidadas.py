#Funciones Anidadas
'''Ejecutar una función dentro de otra función que puede o no recibir los argumentos de
la funcion que la contiene '''

def division(valor_uno,valor_dos):
    variable = "nuevo"
    def validacion():
        print(variable)
        return valor_uno>0 and valor_dos>0
    if validacion():
        return valor_uno/valor_dos
resultado = division(45,4)
print(resultado)