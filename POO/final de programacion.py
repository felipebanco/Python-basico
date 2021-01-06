#Final de programacion
'''
Se necesita un programa que permita manejar el saldo inicial de una cuenta.
El saldo inicial debe de ser de pesos 0.00.
El programa debe solicitar que el usuario indique si desea realizar un depósito o un retiro.
Si el usuario elige realizar un retiro, se solicita un valor y debe de verificar que haya el saldo suficiente
para retirar. De no ser así se envía un mensaje al usuario notificando esa situación. Si hay saldo suficiente,
se resta el valor ingresado al saldo.
Si el usuario elige hacer un depósito se solicita un valor y ese valor se suma al saldo.
Al final de cada transacción se pregunta al usuario si desea realizar otra transacción. Si contesta
afirmativamente, se repiten las acciones anteriores. Si no, se termina el programa, mostrando el saldo
final de la cuenta. Ademas se deberían guardar los distintos retiros y depósitos que realizó el titular
de la cuenta.
'''

from datetime import datetime
saldo_inicial = 0
deposito_de_caja = 0
retiro_de_caja = 0
lista_total = ()

while True:
    print('''\t.BIENVENIDO A SU CAJERO AUTOMATICO. MENÚ:
1). DEPOSITAR DINERO A SU CUENTA.
2). RETIRO DE DINERO DE SU CUENTA.
3). SALIR.''')
    opcion_principal = int(input("INGRESE EL NÚMERO DE OPERACIÓN QUE DESEA REALIZAR: "))

    print()

    if opcion_principal == 1:
        deposito_de_caja = float(input("\nINGRESE EL MONTO A DEPOSITAR: "))
        saldo_inicial += deposito_de_caja
        print(f"\nSU SALDO ACTUAL ES DE ${saldo_inicial}")
        print("¿DESEA REALIZAR OTRA OPERACION?:")
        print("1) SÍ")
        print("2) NO")
        opcion = int(input("INGRESE EL NUMERO DE OPCION: "))
        if opcion == 1:
             print('''\t
             3). DEPOSITAR DINERO A SU CUENTA.
             4). RETIRO DE DINERO DE SU CUENTA.
             ''')
             opcion_principal = int(input("INGRESE EL NÚMERO DE OPERACIÓN QUE DESEA REALIZAR: "))
             if opcion_principal == 3:
                 deposito_de_caja = float(input("\nINGRESE EL MONTO A DEPOSITAR: "))
                 saldo_inicial += deposito_de_caja
                 print(f"\nSU SALDO ACTUAL ES DE ${saldo_inicial}")
             elif opcion == 4:
                 retiro_de_caja = int(input("INGRESE EL MONTO QUE DESEA RETIRAR: "))
                 if retiro_de_caja <= saldo_inicial:
                     saldo_inicial -= retiro_de_caja
                     print(f"SU SALDO ACTUAL ES DE ${saldo_inicial}")
             else:
                print("EL NUMERO INGRESADO NO COINCIDE CON EL NUMERO DE OPERACIONES DISPONIBLES")
                break
    elif opcion_principal == 2:
        retiro_de_caja = int(input("INGRESE EL MONTO QUE DESEA RETIRAR: "))
        if retiro_de_caja <= saldo_inicial:
            saldo_inicial -= retiro_de_caja
            print(f"SU SALDO ACTUAL ES DE ${saldo_inicial}")
        elif retiro_de_caja > saldo_inicial:
            print("EL MONTO INGRESADO ES SUPERIOR AL SALDO DISPONIBLE")
            print("¿DESEA REALIZAR OTRA OPERACION?:")
            print("1) SÍ")
            print("2) NO")
            opcion = int(input("INGRESE EL NUMERO DE OPCION: "))
            if opcion == 1:
                    print('''\t.
                           1). DEPOSITAR DINERO A SU CUENTA.
                           2). RETIRO DE DINERO DE SU CUENTA.
                           ''')
                    opcion_principal = int(input("INGRESE EL NÚMERO DE OPERACIÓN QUE DESEA REALIZAR: "))
            elif opcion == 2:
                    print("GRACIAS POR UTILIZAR SU CAJERO AUTOMATICO")
                    break
            else:
                    print("EL NUMERO INGRESADO NO COINCIDE CON EL NUMERO DE OPERACIONES DISPONIBLES")
                    break

