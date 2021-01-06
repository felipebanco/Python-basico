#Funciones
'''Son un bloque de codigo que permiten resolver un problema especificio y sirven para
reutilizar el codigo cuantas veces queramos, existen funciones con retorno de valor y sin retorno.
Las funciones se incializan con def, luego sigue el nombre de la accion especifica de la funcion,
entre los parentesis van los argumentos
'''

#Funcion sin retorno de valor
def saludar():
    print("Hola")
saludar() #Para que la funcion se ejecute es necesario llamarla fuera de la identacion
print()
def saludar1(nombre):
    print(f"Hola {nombre}")
saludar1("Carla")
print()
def tabla_multiplicar(num):
    for i in range(1,11):
        print(f" {num}*{i} = {num*i}")
tabla_multiplicar(5)
