"Ingresar 10 notas de alumnos y decir cuales son mayores a 7 y menores a 7"

i = 0
notas = 0
notas_Mayores = 0
notas_Menores = 0

while i < 10:
    notas = int(input("Ingrese las notas: "))
    i = i + 1

    if notas >= 7:
        notas_Mayores = notas_Mayores + 1

    elif notas <= 7:
        notas_Menores = notas_Menores + 1


print(f"Existen {notas_Mayores} notas mayores a 7.")
print(f"Existen {notas_Menores} notas menores a 7.")