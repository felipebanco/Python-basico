#Ejercicio 2 "Condicionales"
'''Hacer un programa que pida 3 numeros y determine cual es el mayor'''

num1=int(input("Digite un numero:"))
num2=int(input("Digite un numero:"))
num3=int(input("Digite un numero:"))

if num1>num2 and num1>num3:
    print(f"{num1} es el mayor de los tres numeros ingresados.")
elif num2>num1 and num2>num3:
    print(f"{num2} es el mayro de los tres numeros ingresados.")
else:
    print(f"{num3} es el mayor de los tres numeros ingresados.")

print("Fin del programa.")