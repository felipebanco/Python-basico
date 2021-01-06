#Cadenas de texto "Strings"
'''Para crear un nuevo string como suma solo hace falta usar
"course" mas las variables que se quieren sumar'''

my_string= "Hola Soy Felipe"

name = "Felipe"

course = "Python"
name = 'Felipe'
final_message="Esta es mi primera linea de string en " + course + "por" + name #1 Metodo
final_message="\nEsta es mi primera linea de string en %s por %s " %(course, name)#2 Metodo
final_message="\nEsta es mi primera linea de string en {} por {} ".format(course, name)#3 Metodo
print(my_string)
print(final_message)

