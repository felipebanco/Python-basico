#Excepciones

def dividirNumeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1/num2
            print(f"El resultado de la división es {resultado:.2f}") #Finalizar con dos decimales
        except ValueError:
            '''ValueError: Error por tipo de datos'''
            print("Error N°1 /ValueError/ -> Ingrese correctamente los números")
        except ZeroDivisionError:
            '''ZeroDivisionError: Error porque no se puede dividir por cero'''
            print("Error N°2 /ZeroDivisionError/-> No se puede dividir por 0 ")
        else:
            print("Programa y función finalizados")
            break
dividirNumeros()
