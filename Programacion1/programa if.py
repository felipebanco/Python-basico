
nota = float(input("Digite la nota: "))

if nota <= 0 or nota >= 11:
    print("Error ingrese una calificacion mayor a 0 y menor a 10")

elif nota < 4:
    print("Vuelva en Marzo")
elif nota >= 4 and nota <= 7:
    print("Aprobado")
elif nota >= 8 and nota <= 9:
    print("Bueno")
else:
    print("Excelente")