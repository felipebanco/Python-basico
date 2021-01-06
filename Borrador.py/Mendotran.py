def suma(valor_uno,valor_dos,valor_tres):
    return valor_uno+valor_dos+valor_tres
resultado = suma(10,20,30)
print(resultado)

def multiplicacion(valor_uno,valor_dos):
    return valor_uno*valor_dos
mi_variable = multiplicacion(valor_uno=2, valor_dos=7)
print(f"El resultado es: {mi_variable}")

def multiples_Valores():
    return "String", 1, False, 2.8
string, int, bool, float = multiples_Valores()
print(string)
print(int)
print(bool)
print(float)

def resta(num1,num2):
    return  num1-num2
mi_variable = resta
resultado = mi_variable(45,5)
print(resultado)
