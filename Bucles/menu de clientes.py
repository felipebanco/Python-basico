#Ejercicio 3
'''
Crear un programa que tenga una lista de clientes, cada cliente tiene su nombre, apellido y DNI.
El programa tendrá el siguiente menú de opciones:
 -1 Agregar un nuevo cliente.
 -2 Mostrar todos los clientes.
 -3 Mostrar cliente por DNI.
 -4 Eliminar cliente.
 -5 Salir.
'''

def agregar_cliente(clientes,nombre,apellido,dni):
    cliente = {} #Diccionario
    cliente["nombre"] = nombre
    cliente["apellido"] = apellido
    cliente["dni"] = dni
    clientes.append(cliente) #agregar toda la informacion del diccionario a la lista
clientes = [] #lista vacía

def mostrar_todos_clientes(clientes):
    for i in clientes:
        print(f"nombre: {i[nombre]}, apellido: {i[apellido]}, dni: {i[dni]}")

def mostrar_cliente(clientes,dni):
    for i in clientes:
        if i["dni"] == dni:
            print(f"nombre: {i[nombre]}, apellido: {i[apellido]}, dni: {i[dni]}")
            return True
    return False #En caso de que el dni ingresado no coincida con ninguno de los previamente cargados

def eliminar_cliente(clientes,dni):
    for i in clientes:
        if i["dni"] == dni:
            clientes.remove(i)
            return True
    return False

while True:
    print('''\t.:MENÚ.:
    -1 Agregar un nuevo cliente.
    -2 Mostrar todos los clientes.
    -3 Mostrar cliente por DNI.
    -4 Eliminar cliente.
    -5 Salir.''')
    opcion = int(input("HOLA BIENVENIDO/A, SELECCIONE EL NÚMERO DE OPCIÓN QUE DESEA REALIZAR: "))
    print()

    if opcion==1:
        nombre = input("INGRESE EL NOMBRE DEL CLIENTE: ")
        apellido = input("INGRESE EL APELLIDO DEL CLIENTE: ")
        dni = input("INGRESE EL DNI DEL CLIENTE: ")
        agregar_cliente(clientes,nombre,apellido,dni)

    elif opcion==2:
        mostrar_todos_clientes(clientes)

    elif opcion==3:
        dni = input("INGRESE EL DNI DEL CLIENTE: ")
        if mostrar_cliente(clientes,dni):
            print("CLIENTE ENCONTRADO")
        else:
            print("CLIENTE NO ENCONTRADO")

    elif opcion==4:
        dni = input("INGRESE EL DNI DEL CLIENTE QUE DESEA ELIMINAR: ")
        if eliminar_cliente(clientes,dni):
            print("CLIENTE ELIMINADO")
        else:
            print("CLIENTE NO ENCONTRADO")

    elif opcion==5:
        print("ADIÓS")
        break

    else:
        print("EL NÚMERO INGRESADO NO COINCIDE CON EL NUMERO DE OPERACIÓN")

    print()