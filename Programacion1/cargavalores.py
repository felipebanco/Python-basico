'''Escribir un programa que solicite la carga de un valor positivo y nos muestre
desde 1 hasta el valor ingresado de uno en uno. Ejemplo: Si ingresamos 30 se debe
mostrar en pantalla los números del 1 al 30'''

valor = int(input("Ingrese un valor: "))


for x in range(1,valor+1):
    print(x)
