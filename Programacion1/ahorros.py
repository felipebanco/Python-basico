'''Se requiere un algoritmo para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes desposita variables cantidades de dinero; además, se requiere
saber cuánto lleva ahorrado cada mes.'''


mes = 0
i = 1
meses = ["Enero, Febrero, Marzo, Abril, Mayo, Julio, Junio, Agosto, Septiembre, Octubre, Noveiembre, Diciembre"]
list = []

while i <= 2:
    print('Bienvenido')
    print()
    print(meses)
    print("¿Cuál es el mes en el que desea depositar ahora")
    mes = input("Ingrese el mes: ")

    if mes == "Enero" or "enero":
        valor = int(input("¿Cuanto va a depositar: ?"))
        list.append(valor)
    
    elif mes == "Febrero" or "febrero":
        valor = int(input("¿Cuanto va a depositar: ?"))
        list.append(valor)

print(list)