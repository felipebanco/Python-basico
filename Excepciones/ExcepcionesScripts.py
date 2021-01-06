#Las excepciones sirven para facilitar los errores de ejecución a la hora de escribir código

'''
En las excepciones tambien se pueden definir clases y funciones.
'''

try:
    division=2/0 #Se define el error que se puede presentar
    print(division)
except ZeroDivisionError as ex:#Es necesario definir el error con su nombre tecnico en Except
    print(ex)
    print("\nNo es posible dividir por Cero")  # Lo que se ejecuta y muestra por pantalla ante ese error
try:
    array= [1,2]
    print(array[9])
except IndexError as ex:
    print(ex) #Siempre se debe mostrar por pantalla el tipo de error detectado
    print("\nNo es posible acceder a la posicion solicitada, se encuentra fuera de rango.")
try:
    array=[1,8]
    print(array[11])
except Exception as ex: #La funcion "Exception" clasifica y busca el error sin necesidad de definirlo
    print(ex)
    print("\nSe ha detectado un error en el código")
finally:
    print("\nSe termino el Script") #La funcion finally se ejecuta si o si a pesar que los anteriores errores
    #no se hayan presentado
