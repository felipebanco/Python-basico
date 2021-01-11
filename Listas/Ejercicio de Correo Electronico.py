#Ejercicio 1:
'''•
    Crea un programa que pida introducir una dirección de email por teclado. El programa
    debe imprimir en consola si la dirección de email es correcta o no en función de si esta
    tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
    ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
    o al final, la dirección también será errónea.
'''

e_mail = input("Ingresa tu correo: ")

arroba = e_mail.count("@")

if("@"!=1 or e_mail.rfind("@")==(len(e_mail)-1) or e_mail.find("@")==0):
    print("El e-mail ingresado es incorrecto")
    #Explicación: rfind busca que el @ no este al final de la lista, find busca que no esté al principio
    #len busca que el @ este ingresado.
else:
    print("El e-mail ingresado es correcto")



