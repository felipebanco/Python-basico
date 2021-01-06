#Condicionales Combinados
'''Son condicionales dentro de otros condicionales'''

edad = int(input("Ingrese la edad: "))

if edad>0 and edad<100: #Otra forma de escribirlo: 0<edad<100
    print("El usuario esta vivo")
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

elif edad>=100 or edad<0:
    print("El usuario no esta vivo")







