#Ejercicio 5
'''Hacer un programa que simule un cajero automatico con un saldo incial de $1000
y tendra el siguiente menu de opciones:
-Ingresar dinero a la cuenta.
-Retirar dinero de la cuenta.
-Mostrar el dinero disponible.
-Salir.                         '''

saldo_inicial=1000
saldo=0
retiro=0

print("Bienevenido a su cajero automatico")
print("1)Ingresar dinero a su cuenta")
print("2)Retirar dinero de su cuenta")
print("3)Mostrar el dinero disponible")
print("4)Salir.")


opcion=int(input("\nDigite el numero de operacion que desea realizar: "))

if opcion==1:
    extra= float(input("\nDigite la cantidad de dinero que desea ingresar a su cuenta: "))
    saldo= saldo_inicial + extra
    print(f"\nSu saldo actual es de ${saldo}.")
elif opcion==2:
    retiro = float(input("\nDigite la cantidad de dinero que desea retirar de su cuenta: "))
    if retiro>saldo_inicial:
        print("\nNo tiene suficiente saldo en su cuenta.")
    else:
        saldo= saldo_inicial-retiro
    print(f"\nSu dinero actual disponible es de ${saldo}.")
elif opcion==3:
    print(f"\nSu dinero actual en la cuenta es de ${saldo_inicial}.")
elif opcion==4:
    print("\nGracias por utlizar su cajero automatico.")
else:
    print("\nEl numero ingresado no coincide con ninguna de las operaciones mencionadas")

print("\nFin del programa.")