'Crear un registro de usuario y permitir que se realicen determinadas funciones'

password = ()
e_mail = ()
usuario = {}

print("Bienvenido")
print("1) Registro de Usuario")
print("2) Inicio de Sesión")
print("3) Salir")

opcion = int(input("¿Qué opción desea elegir?: "))

if opcion==1:
    e_mail = input("ingrese un email: ")
    password = input("ingrese una contraseña: ")
    usuario = {'DatosUsuario': {'email': e_mail, 'password': password}}
    print("Usted se ha registrado")
continue

elif opcion==2:

    e_mail = input("ingrese su email: ")
    password = input("ingrese su contraseña: ")

    if e_mail and password == usuario:
        print("hola")
        break
    else:
        print("Vuelva a ingresar sus datos")
        e_mail = input("ingrese su email: ")
        password = input("ingrese su contraseña: ")
        continue

elif opcion == 3:
    print("Ha abandonado el sitio")
    break

else:
    print("ninguna de los números coincide con las opciones anteriores")
    opcion = int(input("¿Qué opción desea elegir?: "))
    continue

'''
print("Registro de Usuario")

e_mail = input("ingrese un email: ")
password = input("ingrese una contraseña: ")
print(usuario)


while True(

    

    if e_mail and password == True{
        break
    }
    else:
        continue
)
'''