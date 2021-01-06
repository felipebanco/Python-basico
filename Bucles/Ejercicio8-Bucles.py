#Ejercicio 8 - Cajero automatico con bucles - Menú iterativo


saldo_inicial=1000
while True:
    saldo=0
    retiro=0

    print("\tBienevenido a su cajero automatico")
    print("\t1)Ingresar dinero a su cuenta")
    print("\t2)Retirar dinero de su cuenta")
    print("\t3)Mostrar el dinero disponible")
    print("\t4)Salir.")


    opcion=int(input("\tDigite el numero de operacion que desea realizar: "))

    if opcion==1:
        extra= float(input("\tDigite la cantidad de dinero que desea ingresar a su cuenta: "))
        saldo= saldo_inicial + extra
        print(f"\tSu saldo actual es de ${saldo}.")
        print()
    elif opcion==2:
        retiro = float(input("\tDigite la cantidad de dinero que desea retirar de su cuenta: "))
        if retiro>saldo_inicial:
            print("\tNo tiene suficiente saldo en su cuenta.")
        else:
            saldo= saldo_inicial-retiro
        print(f"\tSu dinero actual disponible es de ${saldo}.")
        print()
    elif opcion==3:
        print(f"\tSu dinero actual en la cuenta es de ${saldo_inicial}.")
        print()
    elif opcion==4:
        print("\tGracias por utlizar su cajero automatico.")
        break
    else:
        print("\tEl numero ingresado no coincide con ninguna de las operaciones mencionadas")
        print("\tPor favor vuelva a ingresar otro numero que coincida con las opciones mostradas.")
        print()
        continue

print("\nFin del programa.")