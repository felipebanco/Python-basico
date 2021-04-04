#Un string es una lista de caracteres como un arreglo
'''
Un string se comporta como un arreglo de caracteres por ejemplo:
String : 'C o m p u t a d o r a'
[0 1 2 3 4 5 6 7 8 9 10] Posiciones de cada caracter en el string.

'''

my_string="Mi computadora"
print(my_string)
print(my_string[0])#Al marcar entre corchetes un numero del string se imprime el caracter de dicha posicion
print(my_string[0], my_string[-1]) #Si se pone un numero negativo se recorre hacia atras.
print(my_string[3:14]) #Para imprimir una fracción del string
print(my_string [::-1]) #Leer todo el string hacia atras invirtiendo las letras.
