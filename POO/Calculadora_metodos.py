class Calculadora:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    #Metodos
    def sumar(self):
        # Buena practica retornar el valor
        suma = self.num1+self.num2
        return suma

    def restar(self):
        return self.num1-self.num2

    def multiplicacion(self):
        return self.num1*self.num2
    
    def division(self):
        return self.num1/self.num2

    def potencia(self):
        return self.num1**2