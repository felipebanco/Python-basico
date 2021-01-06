#Continue y Break
'''
Tipo de instrucciones que se pueden utlizar en los 3 tipos de bucles. For, While, For range.
'''

for i in range (11):
    if i==5: #Una vez que se encuentra en la posicion 5 la instruccion continue omite dicho elemento
        continue
    print(i)
print("Programa 1 finalizado.")

for i in range (10):
    if i==5: #Cuando el iterador llega a dicho elemento, la instruccion break finaliza la ejecucion del algt.
        break
    print (i)
print("\nPrograma 2 finalizado.")