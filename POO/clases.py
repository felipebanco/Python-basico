class Auto():
    largoChasis = 250 #Atributos
    anchoChasis = 120
    neumaticos = 4
    enMarcha = False
    
    #Los métodos se declaran igual que las funciones y siempre están dentro de una clase
    def arrancar(self): #Self hace referencia al propio objeto 
        self.enMarcha = True

    def estado(self):
        if(self.enMarcha):
            return "El auto está en marcha"       
        else:
            return "El auto está parado"

miAuto= Auto() #Objeto Instanciar o Ejemplar de clase

#El objeto miAuto accede a los atributo y métodos de la clase auto con nomenclatura del punto
miAuto.arrancar()

print(miAuto.largoChasis)
#Se muestran por pantalla las propiedades solicitadas
print(miAuto.estado())

'''
    Primero se verifica el método arrancar y luego el condicional al comprobar que enMarcha es verdadero se devuelve el mensaje.
'''