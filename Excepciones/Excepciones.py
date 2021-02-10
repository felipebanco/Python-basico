#Exepciones:

while True:
    try:
        numero = int(input("Ingrese un número: "))
        print(f"La suma del número es: {numero+10}")
    except: #La excepción muestra un mensaje y permite que el programa pueda seguir la ejecución
        print("Ha ocurrido un error, ingrese un valor de tipo entero")
    else: #Sólo funciona en caso que no se haya dfinido previamnete una excepción
        print("Programa finalizado correctamente")
        break
    finally: #Siempre se ejecuta con el Try y Except
        print("Iteración Finalizada")
