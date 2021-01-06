from datetime import datetime

saldo_inicial = 0
deposito_de_caja = 0
retiro_de_caja = 0
lista_total = []

while True:
    print('''
\tBienvenido!
Menu:
1) Depositar dinero en su cuenta
2) Retirar dinero de su cuenta
3) Mostrar Movimientos
    ''')
    opcion1 = int(input("Ingrese el número de operación: "))

    if opcion1 == 1:
        lista_deposito = [] #Lista donde se guardan todos los datos de deposito
        deposito_de_caja = float(input("Ingrese la cantidad de dinero que desea depositar: "))
        saldo_inicial += deposito_de_caja # saldo inicial = saldo inicial + deposito
        hora_deposito = datetime.now() #Funcion que guarda la hora y la fecha
        print(f"Su saldo actual es de ${saldo_inicial}")
        lista_deposito.append(hora_deposito.day)
        lista_deposito.append("-")
        lista_deposito.append(hora_deposito.month)
        lista_deposito.append("-")
        lista_deposito.append(hora_deposito.year)
        lista_deposito.append("  ")
        lista_deposito.append(hora_deposito.hour)
        lista_deposito.append(":")
        lista_deposito.append(hora_deposito.minute)
        lista_deposito.append(":")
        lista_deposito.append(hora_deposito.second)
        lista_deposito.append("  Depósito  ")
        lista_deposito.append(deposito_de_caja)
        lista_total.append(lista_deposito)
        deposito_de_caja = 0


    elif opcion1 == 2:
        lista_retiro = []
        retiro_de_caja = int(input("Ingrese la cantidad de dinero que desea retirar: "))
        if retiro_de_caja>saldo_inicial:
            print("No tiene saldo suficiente")
        else:
            saldo_inicial -= retiro_de_caja
            hora_retiro = datetime.now()
            print(f"Su saldo actual disponible es de {saldo_inicial}")
            lista_retiro.append(hora_retiro.day)
            lista_retiro.append("-")
            lista_retiro.append(hora_retiro.month)
            lista_retiro.append("-")
            lista_retiro.append(hora_retiro.year)
            lista_retiro.append("  ")
            lista_retiro.append(hora_retiro.hour)
            lista_retiro.append(":")
            lista_retiro.append(hora_retiro.minute)
            lista_retiro.append(":")
            lista_retiro.append(hora_retiro.second)
            lista_retiro.append("  Retiro  ")
            lista_retiro.append(retiro_de_caja)
            lista_total.append(lista_retiro)
            retiro_de_caja = 0

    else:
        for i in lista_total:
            print(*i) #funcion que ordena el historial de movimientos

    print(f"Saldo a la fecha: {saldo_inicial}")

    while True:
        print("¿Desea realizar otra operación: ")
        print("1) Si")
        print("2) No")
        opcion2 = int(input("Digite el número de operación: "))

        if opcion2 == 1:
            break
        elif opcion2 == 2:
            break
        else:
            print("Opción inválida, seleccione una de las disponibles: ")
            continue

    if opcion2 == 2:
        break
    else:
        continue

print("Gracias por utilizar nuestro cajero")
