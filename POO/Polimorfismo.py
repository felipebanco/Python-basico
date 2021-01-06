#Polimorfismo
"""
Concepto que se hace referencia a un objeto que cambia de forma y a la vez de comportamiento
"""

class Auto():
    def desplazamiento(self):
        print("Un automóvil se desplaza por medio de cuatro ruedas.")

class Motocicleta():
    def desplazamiento(self):
        print("Una motocicleta se desplaza por medio de dos ruedas.")

class Camion():
    def desplazamiento(self):
        print("Un camión se desplaza utlizando seis ruedas.")

#Metodo 1 para aplicar polimorfismo
miMoto=Motocicleta()
miMoto.desplazamiento()
miauto=Auto()
miauto.desplazamiento()
#Metodo 2 para aplicar polimorfismo()
def desplazamientoVehiculo(vehiculo): #Crea una funcion genérica con un objeto genérico.
    vehiculo.desplazamiento()         #Se le asigna un método.
miVehiculo= Camion()                  #Se crea dicho objeto y se le asigna la clase solicitada.
desplazamientoVehiculo(miVehiculo)    #Se intercambian los valores y se imprime por pantalla.