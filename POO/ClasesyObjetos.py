class Auto():
    '''El constructor init define un estado inicial (características comunes) de todos los objetos pertenecientes una clase'''
    def __init__(self,largoChasis,anchoChasis,ruedas,enmarcha):
        self.__largoChasis =  250# largoChasis es una variable que contiene el valor que llega
        self.__anchoChasis = 120  #por parámetro, self.largoChasis es el atributo de la instancia
        self.__ruedas = 4    #Lss __ son del encapsulamiento del atributo, para que no sea modificado.
        self.__enMarcha = False

    #Cada vez que se definen constructores y métodos se utiliza self, para hacer referencia al propio objeto.
    def arrancar(self,arrancamos):
        self.__enMarcha = arrancamos #Accede al atributo del objeto definido en el cosntructor.

        if(self.__enMarcha): #En un condicional si no se declara True or False, el valor por defecto es True.
            chequeo= self.__chequeo_interno() #Se asocia en una variable "True or False"

        if(self.__enMarcha and chequeo): #Chequeo=True
            return "El auto se encuentra en marcha."
        elif(self.__enMarcha and chequeo == False):
            return  "Algo salió mal, revise sus niveles de aceite,combustible etc."
        else:
            return "El auto se encuentra parado."

    def estado(self): #Método que informa de las propiedades del objeto.
        print("El auto tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "m.", "Y un largo de", self.__largoChasis, "m.")

    def __chequeo_interno(self): #Método Encapsulado
        print("Se está realizando un chequeo interno.")
        self.gasolina = "Nivel de combustible suficiente."
        self.aceite = "Nivel de aceite suficiente."
        self.puertas = "Todas las puertas están cerradas."

        if(self.gasolina == "Nivel de gasolina suficiente." and self.aceite == "Nivel de aceite suficiente." and self.puertas == "Todas las puertas están cerradas." ):
            return True
        else:
            return False


print("<-------------A continuación el primer objeto------------->")
miAuto = Auto("largoChasis","anchoChasis","ruedas","enMarcha") #Instanciar una clase, asociar un objeto a la misma.
print(miAuto.arrancar(True))#Asociar el objeto al método de la clase, el valor que toma arrancar en el parámetro arrancamos es True.
#Como el método arrancar devuelve un string, se debe utilizar print para llamarlo.
miAuto.estado()
print()

print("<-------------A continuación el segundo objeto------------->")
miAuto2 = Auto("largoChasis","anchoChasis","ruedas","enMarcha")
print(miAuto2.arrancar(False))
miAuto2.estado()

