'''
Un palindromo es un numero o cadena que se lee igual de izquierda a derecha y visceversa
'''
def palindromo(frase):
    frase = frase.replace(" ", "") #Remplaza espacios por nada
    print(frase) #Variables Locales: Se encuentran dentro de la funcion
    return frase == frase[::-1] #Recorre toda la cadena como una lista y la regresa al reves
frase = "anita lava la tina"
resultado = palindromo(frase)
print(f"Frase original->{frase}") #Variables Globales: Se encuentran fuera de la funcion
print(resultado)
print()
def valor_global():
    global variable_global #Modificar variables globales
    variable_global = "Cambiar valor"
variable_global = "esto es una variable global"
print(variable_global)
valor_global()
print(variable_global)
print()
def crear_variable_global():
    global nueva_variable
    nueva_variable = "This is a global variant"
crear_variable_global()
print(nueva_variable)
