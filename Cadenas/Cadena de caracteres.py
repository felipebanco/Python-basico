#Cadena de caracteres.

cadena = "Estoy 'programando'"
print(cadena)

cadena1 = "Estoy \"Estudiando\"" #Imprimir comillas dentro de la cadena
print(cadena1)

cadena2 = r"D:\Nombre\trabajos" #Imprimir toda la cadena en crudo
print(cadena2)

cadena3 = "Felipe"
print(cadena + cadena1) #Unir cadenas

cadena4 = "Banco"
cadena4 = 'b' + cadena4[1:] #Se agrega la letra 'b' en adelante
print(cadena4)
print(len(cadena4)) #Calcular la cantidad de caracteres