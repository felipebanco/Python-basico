#Conjuntos parte 2
'''Operaciones que se pueden realizar con los conjuntos:
   -Union
   -Interseccion.
   -Diferencia
   -Diferencia simetrica'''

a = {1, 2, 3}
b = {3, 4, 5} #Siempre y cuando los elementos sean los mismos, no importa el orden siguen siendo iguales.
c = a | b #Metodo para calcular la union o suma de dos conjuntos.
c = a & b #Metodo para calcular la intersección es decir que elementos tiene en comun ambos conjuntos.
c1 = a - b #Metodo para calcular la diferencia es decir los elementos que solo se encuentran en un conjunto.
c2 = a ^ b #Metodo para calcular la diferencia simetrica es decir todo lo que esta fuera de la interseccion.
c3 = {1, 2, 3, 4, 5,}
d = frozenset({6, 7, 8, 9})#Metodo para que un conjunto sea inmutable es decir no se puede modificar.

print(a == b)#Metodo para calcular la igualdad entre 2 conjuntos.
print(len(a))#Metodo para calcular cuantos elementos tiene el conjunto a.
print(c)
print(c1)
print(c2)
print(a.issubset(c3))#Metodo para preguntar si un conjunto esta dentro de otro conjunto.
print(c3.issuperset(a))#Metodo para preguntar si c3 es el super conjunto de a.
print(a.isdisjoint(b))#Metodo para preguntar si a y b no comparten ningun elemento en comun.
print(d)