'''Realice un programa que permita cargar 2 listas de 15 valores cada una.
    Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor
    (mensajes lista1 mayor, lista2 mayor, listas iguales). Tener en cuenta que puede
    haber dos o mas estrucuturas repetidas en un algoritmo'''



while True:
    lista1 = []
    lista2 = []
    suma1 = 0
    suma2 = 0
    for i in range(15):
        v1= int(input("Ingrese unos valores: "))
        lista1.append(v1)
    for a in lista1:
        suma1+=a
    print()
    print('Se terminaron de cargar los valores de la lista 1')    
    print()

    for x in range(15):
        v2= int(input("Ingrese más valores: "))
        lista2.append(v2)
    for b in lista2:
        suma2+=b
    print()
    print('Se terminaron de cargar los valores de la lista 2')
    print()

    if(suma1 > suma2):
        print("Lista 1 Mayor")
        print()
        print('Lista 1 es igual a ',suma1)

    elif(suma1 < suma2):
        print("Lista 2 Mayor")
        print()
        print('Lista 2 es igual a ',suma2)

    else:
        print('Ambas listas son iguales')




