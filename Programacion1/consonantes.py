palabra = input("Ingrese una palabra: ")
vocales = ["a","e","i","o","u"]
cantidad_vocales = 0
consonantes = 0
digitos = 0
espacio = 0
otros = 0

for x in palabra:

    if x.isalpha():
        if x in vocales:
            cantidad_vocales+=1
        else:
            consonantes+=1
    elif x.isnumeric():
        digitos+=1
    elif x.isspace():
        espacio+=1
    else:
        otros+=1
print(consonantes)
print(cantidad_vocales)
print(digitos)
print(espacio)
print(otros)