#Herencia I

class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha = False
        self.acelerar = False
        self.frenar = False
    def arrancar(self):
        self.enMarcha=True
    def acelerar(self):
        self.acelerar = True
    def frenar(self):
        self.acelerar = True
    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",self.enMarcha
            ,"\nAcelerando: ",self.acelerar, "\nFrenando: ",self.frenar)

class Camioneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if (self.cargado): #Se asume que la variable cargado es True
            return "La camioneta se encuentra cargada"
        else:
            return "La camioneta no está encuentra cargada."

class Moto(Vehiculos): #Herencia: Recibe todos los atributos, métodos y constructores de la clase padre.
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo caballito."
    def estado(self): #Métdo que se sobreescribe en el método de la clase padre
        print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",self.enMarcha
            ,"\nAcelerando: ",self.acelerar, "\nFrenando: ",self.frenar, "\nAcrobacia: ",self.hcaballito)

class VehiculosElectricos(Vehiculos): #Clase independiente.
    def __init__(self,marca,modelo):
        super(). __init__(marca,modelo)
        self.autonomia = 100
    def cargarEnergia(self):
        self.cargando = True

class BicicletaElectrica(VehiculosElectricos,Vehiculos): #Herencia múltiple, hereda métodos y atributos de dos clases
    def estado(self):#Se da preferencia a la primera clase a la que se le asigna la herencia.
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha
        , "\nAcelerando: ", self.acelerar, "\nFrenando: ", self.frenar)


print("Primer objeto: Mi Moto")
MiMoto = Moto(marca="Yamaha",modelo=2010) #Objeto de la clase moto.
MiMoto.caballito()
MiMoto.estado()
print()
print("Segundo objeto: Mi Camioneta")
MiCamioneta=Camioneta(marca="Toyota",modelo=2017)
print(MiCamioneta.carga(True))
MiCamioneta.estado()
print("Tercer objeto. Mi Bicicleta Electrica    ")
MiBicicleta=BicicletaElectrica(marca="Venzo",modelo="345-678")
MiBicicleta.estado()



