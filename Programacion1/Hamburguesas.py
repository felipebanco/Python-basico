
costo_Total = 0
costo_Principal = 0
costo_Tarjeta = 1.05
costo_Total_Efectivo = 0


while True:

    print("Bienvenido, ¿Qué desea llevar?")
    print()
    print("1) Hamburguesa sencilla = $20.00")
    print("2) Hamburguesa doble = $25.00")
    print("3) Hamburguesa triple = $28.00")


    tipo = int(input("Ingrese el numero que corresponda al tipo de hamburguesa que va a llevar: "))
    cantidad = int(input("Ingrese la cantidad de hamburguesas que va llevar: "))
    print()
    print("Las formas de pago que aceptamos son las siguientes: ")
    print("1) Tarjeta")
    print("2) Efectivo")
    tipo_Pago = int(input("Seleccione la opción con la que desea abonar:  "))

    if tipo == 1:

        if tipo_Pago == 1:
                costo_Principal = 20 * cantidad
                costo_Total = costo_Principal * costo_Tarjeta
                print(f"El costo total de su pedido de {cantidad} hamburguesas de tipo Sencilla "
              f"con el recargo del 5% es de ${costo_Total}.")
        elif tipo_Pago == 2:
                costo_Total_Efectivo = 20 * cantidad
                print(f"El costo total de su pedido de {cantidad} hamburguesas de tipo Sencilla "
              f"es de ${costo_Total_Efectivo}.")

    elif tipo == 2:

        if tipo_Pago == 1:
                costo_Principal = 25 * cantidad
                costo_Total = costo_Principal * costo_Tarjeta
                print(f"El costo total de su pedido de {cantidad} hamburguesas de tipo Doble"
              f"con el recargo del 5% es de ${costo_Total}.")

        elif tipo_Pago == 2:
                costo_Total_Efectivo = 25 * cantidad
                print(f"El costo total de su pedido de {cantidad} hamburguesas de tipo Doble"
                f"de ${costo_Total_Efectivo}.")

    elif tipo == 3:

         if tipo_Pago == 1:
                costo_Principal = 28 * cantidad
                costo_Total = costo_Principal * costo_Tarjeta
                print(f"El costo total de su pedido de {cantidad} hamburguesas de tipo Triple"
              f"con el recargo del 5% es de ${costo_Total}.")

    elif tipo_Pago == 2:
                costo_Total_Efectivo = 28 * cantidad
                print(f"El costo total de su pedido de {cantidad} hamburguesas de tipo Triple es"
              f"de ${costo_Total_Efectivo}.")
                break

    else:
            print("La opción ingresada no concide con ninguna de las anteriores")
            continue