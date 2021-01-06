# PROYECTO FINAL PROGRAMACION

saldo_inicial = 0
deposito = 0
retiro = 0


while True:
    print("1.) Deposito")
    print("2.) Retiro")
    opcion = int(input("Digite la opcion deseada: "))

    #El usuario va a realizar la opcion que desee hacer

    if opcion == 1:
        deposito = int(input("Ingrese el monto a depositar: "))
        saldo_inicial = saldo_inicial + deposito
        print(f"Su saldo actual es de: {saldo_inicial}")
    elif opcion == 2:
        retiro = int(input("Ingrese el monto a retirar: "))
        if retiro <= saldo_inicial:
            saldo_inicial= saldo_inicial - retiro
            print(f"Su saldo actual es de: {saldo_inicial}")
        else:
            print("Su saldo es insuficiente para realizar esta operacion")
    else:
        print("La opcion ingresada es incorrecta:")

    while True:
        print("Desea realizar otra operacion?: ")
        print("1.) Si")
        print("2.) No")
        opcion2 = int(input("Digite la opcion que desea realizar: "))
        if opcion2 == 2:
            break
        elif opcion2 == 1:
            break
        else:
            print("la opcion ingresada es incorrecta:")
            continue

    if opcion2 == 2:
        break

print("\nGracias por utilizar nuestros servicios bancarios")


