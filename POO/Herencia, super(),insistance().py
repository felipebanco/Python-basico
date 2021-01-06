#Herencia II

class Persona():
    def __init__(self,nombre,edad,residencia): #Constructor,estado inicial de la clase
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia
    def descripcion(self):
        print("Nombre:",self.nombre,",Edad:",self.edad,"años",",Lugar de residencia:",self.residencia)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,puesto,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        #Instrucción super, permite heredar los atributos de la clase persona y ahorrar código."
        self.salario=salario
        self.antiguedad=antiguedad
        self.puesto=puesto
    def descripcion(self):
        super().descripcion()
        print("Salario:$",self.salario,"Antigüedad:",self.antiguedad,"Puesto:",self.puesto)


MiEmpleado=Empleado(salario=50000,antiguedad=12,puesto="Administrativo.",nombre_empleado="Alejandro",edad_empleado=34,
                    residencia_empleado="Mendoza,Argentina.")
print(MiEmpleado.descripcion())
print(isinstance(MiEmpleado,Empleado)) #Verifica si un objeto pertenece a dicha clase
