#Funciones
def sumar(x,y):
    print("El resultado de la suma es",x+y)
def restar(x,y):
    print("El resultado de la resta es",x-y)
def multiplicar(x,y):
    print("El resultado de la multiplicacion es",x*y)
def dividir(x,y):
    print("El resultado de la division es",x/y)

def suma1(a,b, resultado):
    a=int(input("ingresa: "))
    b= int(input("ingresa: "))
    resultado= a+b
    return resultado
print(suma1('a','b','resultado'))


#Llamado de Funciones
sumar(x=13,y=4)
restar(x=45,y=15)
multiplicar(x=6,y=7)
dividir(x=54,y=12)