'''
Ejercicio 1: Desarrolar un programa que realice un cambio de divisas de moneda local a dólar y visceversa.
'''

usd= int

def cambio_ars_dolares(ars):
    return (ars * 1)/60

def cambio_usd_ars(usd):
    return (usd * 60)/1

while True:
    print('''\t.MENÚ:
1). CONVERTIR DE ARS A USD.
2). CONVERTIR DE USD A ARS.
3). SALIR DEL CONVERTIDOR.''')
    opcion = int(input("INGRESE EL NÚMERO DE OPERACIÓN QUE DESEA REALIZAR: "))

    print()

    if opcion == 1:
        ars = float(input("INGRESE LA CANTIDAD DE PESOS ARGENTINOS QUE DESEA CONVERTIR: "))
        print(f"LA CANTIDAD INGRESADA EN PESOS ES EQUIVALENTE A $USD{cambio_ars_dolares(ars):.2f}")
        break
    elif opcion == 2:
        usd = float(input("INGRESE LA CANTIDAD DE DÓLARES QUE DESEA CONVERTIR: "))
        print(f"LA CANTIDAD INGRESADA EN DÓLARES ES EQUIVALENTE A $ARS{cambio_usd_ars(usd):.2f}")
        break
    elif opcion == 3:
        print("ADIÓS")
        break
    else:
        print("OPCIÓN INVÁLIDA INGRESE EL NUMERO QUE CORRESPONDE A CADA OPERACIÓN")
        break
