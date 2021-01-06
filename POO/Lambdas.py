#Lambda
'''
Permite modificar funciones para que sean anonimas en una sola línea de código
Las lambdas no admiten bucles y condicionales, toda la operación debe de ejecutarse en una sola linea
de codigo
'''

mi_funcion= lambda valor_uno, valor_dos: valor_uno+valor_dos
resultado = mi_funcion(10,20)
print(resultado)