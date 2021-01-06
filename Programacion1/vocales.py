palabra = input("Ingrese una palabra")
vocales = ["a","e","i","o","u"]
total = 0

for x in range(len(vocales)):
    total = palabra.count(vocales[x])
    print("Total vocales",vocales[x],"",total)
