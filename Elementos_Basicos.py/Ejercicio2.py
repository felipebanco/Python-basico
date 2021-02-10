#Ejercicio 2 elementos basicos.
''' Determinar la solución lógica para la siguiente expresión '''

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
resultado = 0

resultado =((3+5*8)<3and((-6/3*4)+2<2))or(a>b)

print(f"El resultado de la siguiente operacion es: {resultado}")

'''((3+5*8)<3and((-6/3*4)+2<2))or(a>b)
   (43<3    and (-8+2<2)) or (10>5)
   ( False  and   True)   or  True
           False          or True 
                    True         '''
