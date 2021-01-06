#Ejercicio 11 - Bucles - Agenda telefonica.
'''Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave
sea el nombre del usuario y el valor sea el número de teléfono, el programa tendrá el
siguiente menú de opciones:
 -Agregar contacto.
 -Borrar contacto.
 -Ver contactos existentes.
 -Salir.
'''

agenda = {}

while True:
    print("\tBienvenido/a a su agenda telefónica")
    print("\t1).Agregar contacto.")
    print("\t2).Eliminar contacto.")
    print("\t3).Ver contactos existentes.")
    print("\t4).Salir de la agenda.")
    print()
    opcion = int(input("Seleccione una de las siguientes operaciones: "))

    print()

    if opcion == 1:

        nombre = input("Escriba el nombre del contacto: ")
        numero_telefono = int(input("Escriba el numero de telefono del contacto: "))
        if nombre or numero_telefono not in agenda: #Si el nombre no esta en la lista entonces se agrega.
            agenda[nombre] = numero_telefono
            print(f"\nSe ha agregado el contacto {agenda}")
        else:
            print("\nEl contacto ya existe.")

    elif opcion == 2:

        nombre = input("\nEscriba o seleccione el contacto que desea borrar: ")
        if nombre in agenda: #Si el nombre esta en la agenda se procede a borrarlo
            del(agenda[nombre])
            print("\nContacto eliminado")
        else:
            print("\nEl contacto no existe.")

    elif opcion == 3:

        print("\nAgenda de contactos: ")
        for clave,valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")

    elif opcion == 4:

        print("¿Desea salir de la agenda de contactos?")
        print("5) Si")
        print("6) No")
        salida = input("Seleccione una opcion: ")
        if salida == 5:
            print("\nGracias por utlizar su agenda de contactos")
            break
        elif salida == 6:
            continue
    else:
        print("\nError, seleccione una de las opciones disponibles")
