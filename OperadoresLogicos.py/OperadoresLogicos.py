# Operadores Lógicos

'''
-Permiten construir expresiones logicas que dan como resultado un valor booleano.
And(Conjunción): True, True: True.
Or(Disyunción): False, False: False.
Not(Negación): not(true): False.
               not(Flase): True.
-La prioridad de los operadores lógicos es la siguiente.
1)Not
2)And
3)Or
-Prioridad de todos los operadores en general:
1. (): Parentesis.
2. **: Exponente.
3. *,/,Mod,Not: Multiplicación, División, Módulo, Negación.
4. +,-,And: Más, Menos, Conjunción.
5. <, <=, >, >=, ==, !=, Or: Menor, Menor igual, Mayor, Mayor igual, Igualdad, Diferencia, Disyunción.
'''

a = 10
b = 12
c = 13
e = 10
f = 15
g = 20

expresion1 = ((a>b)or(a<c))and((a==c)or(a>=b))
print(expresion1)
'''((a>b)or(a<c))and((a==c)or(a>=b))
   (false or true)and(false or false)
        (true    and     false)     
                false              '''

expresion2 = ((e<f)and(f<g))
print(expresion2)

expresion3 = not((e>f)or(f<g))
print(expresion3)
