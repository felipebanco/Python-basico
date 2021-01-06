#Funciones con retorno de valor

#Funcion que multiplica dos numeros
def multiplicar(num1,num2):
    num1= int(input("Digite un numero: "))
    num2= int(input("Digite un numero"))
    mult = num1 * num2
    return mult #Retorna un valor

mult = multiplicar('num1','num2') #Metodo 1 para retornar un valor
print(mult)

print(multiplicar('num1','num2')) #Metodo 2 para retornar un valor
print(multiplicar('num1','num2'))