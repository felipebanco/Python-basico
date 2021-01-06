#Ejercicio 9
'''Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase
pero sin espacios en blanco y ademas un contador de cuantos caracteres tiene la frase
(sin contar los espacios en blanco).'''

frase= input("Escriba una frase: ")
frase2 = "" #frase vacia para almacenar

for i in frase:
    if i!=" ": #Si el iterador es distinto de los espacios.
        frase2 += i #Se agrega un caracter a la frase vacia.
frase = frase2

print(f"\nLa frase final sin espacios es: {frase}.")
print(f"El N° de caracteres es: {len(frase)}.") #Contador de caracteres.
