#Generadores
'''
Estructuras que extraen valores de una función y se almacenan en objetos iterables (pueden ser
recorridos por bucles), utiliza la palabra reservado Yield
Los generadores entre llamada y ejecución entran en us estado de suspension
'''

#Función Tradicional
def generaPares(limite):
    num = 1
    listaPares = [] #lista vacia que guarda los numeros pares
    while num < limite:
        listaPares.append(num*2) #agregar números al final de la lista al multiplicarlos por 2
        num +=1
    return listaPares
print(generaPares(10))
#Generador
def generaPares(limite):
    num = 1
    while num < limite:
        yield num*2
        num +=1
devuelvePares= generaPares(10)
'''
for i in devuelvePares:
    print(i)
2
4
6
8
etc
'''
print(next(devuelvePares)) #devuelve solo el primer elemento del objeto
print()
print(next(devuelvePares))
print()
print(next(devuelvePares))

