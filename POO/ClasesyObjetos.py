#Clases
'''
Las clases almacenan objetos que a su vez estos mismo poseen un estado, atributos y comportamientos.
Se definen con la palabra reservada class y el nombre en mayúscula.
'''
class Coche():
    '''El constructor init define un estado inicial de todos los objetos pertenecientes a la clase'''
    def __init__(self,largoChasis,anchoChasis,ruedas,enmarcha):
        self.__largoChasis =  250# largoChasis es una variable que contiene el valor que llega
        self.__anchoChasis = 120  #por parámetro, self.largoChasis es el atributo de la instancia
        self.__ruedas = 4    #Lss __ son del encapsulamiento del atributo, para que no sea modificado.
        self.__enMarcha = False

    def arrancar(self,arrancamos):
        self.__enMarcha = arrancamos

        if(self.__enMarcha):
            chequeo= self.__chequeo_interno() #Se asocia en una variable "True or False"

        if(self.__enMarcha and chequeo): #Chequeo=True
            return "El auto se encuentra en marcha."
        elif(self.__enMarcha and chequeo == False):
            return  "Algo salió mal, revise sus niveles de aceite,gasolina etc."
        else:
            return "El auto se encuentra parado."

    def estado(self):
        print("El auto tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "m.", "Y un largo "
            "de", self.__largoChasis, "m.")

    def __chequeo_interno(self): #Método Encapsulado
        print("Se está realizando un chequeo interno.")
        self.gasolina = "Nivel de gasolina suficiente."
        self.aceite = "Nivel de aceite suficiente."
        self.puertas = "Todas las puertas están cerradas."

        if(self.gasolina == "Nivel de gasolina suficiente." and self.aceite ==
        "Nivel de aceite suficiente." and self.puertas == "Todas las puertas están cerradas." ):
            return True
        else:
            return False

print("<-------------A continuación el primer objeto------------->")
miCoche = Coche("largoChasis","anchoChasis","ruedas","enMarcha")  #Instanciar una clase, asociar un objeto a la misma.
print(miCoche.arrancar(True)) #Asociar el objeto al método de la clase.
miCoche.estado()
print("<-------------A continuación el segundo objeto------------->")
miCoche2 = Coche("largoChasis","anchoChasis","ruedas","enMarcha")
print(miCoche2.arrancar(False))
miCoche2.estado()

