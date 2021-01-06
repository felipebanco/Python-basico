#Argumentos por valor o por referencia.
'''
Un argumento por valor es cuando una funcion recibe una copia de dicho argumento y el original no se modifica.
'''

def doblar_numero(numero):
    numero *= 2 #Aqui se realiza la operacion y recibe una copia de n
    print(numero)
n = 5
doblar_numero(n) #n se mantine igual
print(n)
