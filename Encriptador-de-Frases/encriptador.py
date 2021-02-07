#Encriptador

#"Servicio a la comunidad"
#Caracter elegido: "xX"
# Sxrvxcxx x lx cxmxnxdxd

#Variables para modificar el programa:
caracter_elegido = ""

def encriptar(frase, caracter):
    frase_encriptada = "" #Aquí se van guardando los caracteres encriptados de la frase, en una variable vacía
    caracter_elegido = input("Ingresa un carcater con el que quieres encriptar: ")

    for letra in frase:
        if letra.lower() in "aeiouáéíóú": #Se envian y recorren las letras como minúsculas
            if letra.isupper(): #Si la letra es mayúscula
                frase_encriptada = frase_encriptada + caracter_elegido.upper()
            else:
                frase_encriptada = frase_encriptada + caracter_elegido
        else:
            frase_encriptada = frase_encriptada + letra
    
    return frase_encriptada

print(encriptar(input("Ingresa una frase: \n>"), 'caracter_elegido')) #Salto de línea e ingreso de parámetro
