#Lanzar nuestras propias excepciones

def verificandoEdad(edad):
    if edad<0 or edad==0:
        #Mi propia excepción
        raise ValueError ("La edad no puede ser negativa o la persona no existe")
    elif edad<18:
        print("Usted es menor de edad")
    elif edad>18:
        print("Usted es mayor de edad")
    elif edad<30:
        print("Usted es joven")
    elif edad>50:
        print("Usted es un adulto mayor")
    elif edad>80:
        print("Usted es anciano")
edad = int(input("Ingrese su edad: "))
try:
    verificandoEdad(edad)
except ValueError as EdadNegativa: #Renombrar la excepción
    print(EdadNegativa)
print("Programa Finzalizado")