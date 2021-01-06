#Ejercicio 3 Condicionales
'''Hacer un programa que pida un caracter e indique si es una vocal o no'''

letra=input("Digite una letra: ").lower()#Funcion que guarda todos los caracteres en miniscula

if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print(f"La letra ingresada {letra} si es una vocal.")
else:
    print(f"La letra ingresada {letra} no es una vocal.")
