#Argumentos y Parámetros.

def restar(num1,num2): #Cuando se crea una funcion los valores que recibe son parametros
    return num1 - num2
print(restar(4,3)) #cuando se llama a una funcion los valores que recibe son argumentos
print(restar(num2=4,num1=2)) 

def sumar(num1,num2,suma):
    num1=int(input("Ingrese un numero: "))
    num2=int(input("Ingrese un numero: "))
    suma = num1 + num2
    return suma
print(sumar("num1","num2","suma"))

def suma(*args): #El asterisco indica que puede recibir n cantidad de valores
    resultado = 0     #Los valores se devuelven en tuplas
    for valor in args:
        resultado = resultado + valor
    return resultado
resultado = suma(1,2,3,4,5,6,7,8,9,10)
print(resultado)

def suma1(**kwargs): #Los ** clasifican los argumentos segun el tipo de dato
    print(kwargs)    #Los valores se muestran en formato de diccionario
resultado1 = suma1(valor_uno=3, y=True, nombre= "Felipe", x=2.56)
print(resultado1)
