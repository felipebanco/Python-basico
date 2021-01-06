#Ejercicio 1 "Condiconales"

'''Hacer un programa que pida dos numeros y se de cuenta cual de ellos es par, o si
ambos lo son'''

numero1=int(input("Digite un numero para verificar si es par o impar: "))
numero2=int(input("Digite un segundo numero para verificar si es par o impar: "))



if numero1%2==0 and numero2%2==0:
     print(f"{numero1} y {numero2} son numeros pares.")
elif numero1%2==0 and numero2%2!=0:
     print(f"{numero1} es numero par.")
     print(f"{numero2} es numero impar.")
elif numero1%2!=0 and numero2%2==0:
     print(f"{numero1} es numero impar.")
     print(f"{numero2} es numero par.")
else:
    print(f"{numero1} y {numero2} son numeros impares.")

print("Fin del programa.")