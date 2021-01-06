#Yield From
'''
Se utiliza para simplificar el código de generadores en caso de bucles anidados
por ej: Un bucle for dentro de otro bucle for
'''

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield from elemento #Recorre las letras del primer elemento Madrid
ciudades_devueltas = devuelveCiudades("Madrid","Barcelona","Bilbao","Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

largoChasis = 250
anchoChasis = 120
ruedas = 4
enmarcha = False


def __init__(self, largoChasis, anchoChasis, ruedas, enmarcha):
    self.largoChasis = largoChasis  # largoChasis es una variable que contiene el valor que llega
    self.anchoChasis = anchoChasis  # por parámetro, self.largoChasis es el atributo de la instancia
    self.ruedas = ruedas
    self.enMarcha = False

'''
    self.enMarcha = True
    print("El auto está en marcha.")


def detener(self):
    self.enMarcha = False
    print("El auto está parado.")
'''

miCoche = Coche(250,120,4,False)
miCoche2 = Coche(250,120,4,False)
