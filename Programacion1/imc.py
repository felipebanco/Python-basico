"Hacer un programa que calcule el imc"

peso = float(input("Por favor ingrese su peso:"))
altura = float(input("Por favor ingrese su altura: "))
edad = int(input("Por favor ingrese su edad: "))
imc = 0

imc = peso / (altura**altura)

if edad < 45:
    if imc < 22:
        print("Baja")
    elif imc >= 22:
        print("Medio")
elif edad >= 45:
    if imc < 22:
        print("Medio")
    elif imc >= 22:
        print("Alto")