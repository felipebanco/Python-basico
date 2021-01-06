#Funciones con retorno de valor
'''Para retornar un valor existen 2 metodos:
-#1 Almacenar la operacion en una variable y despues imprimirla
-#2 Mostrar la funcion pero definiendo los parametros
Tambien se pueden retornar multiples valores'''

def multiplicacion(num1,num2): #Metodo 1
    multiplicar = num1 * num2
    return multiplicar
multiplicar = multiplicacion(2,4)
print(multiplicar)
print()
def adicion(a,b): #Metodo 2
    suma = a + b
    return suma
print(adicion(7,8))
print()
def prueba():
    return 12,"nombre", [1,2,3,4,5,6] #Se almacenan en una tupla
print(prueba())
print()
def prueba2():
    return "hola", 45, [1,3,6,7,8,9,2,3,]
c,n,l = prueba2()  #Almacena todo el contenido de la funcion en 3 variables
print(c) #cadena
print(n) #entero
print(l) #lista