

def ingresar_datos(nombre,apellido,edad,sexo,usuario):
    usuario= int(input("Ingrese su número de usuario: "))
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    edad=int(input("Ingrese su edad: "))
    sexo=input("ingrese su género: ")
    lista_de_datos= [usuario,nombre,apellido,edad,sexo]

    return lista_de_datos
lista_de_datos= ingresar_datos("usuario","nombre","apellido","edad","sexo")
print(lista_de_datos)

def suma(num1,num2):
    print(num1+num2)
suma(2,3)
suma(4,5)
suma(6,7)



