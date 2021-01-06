vocales = ["a","e","i","o","u"]
palabra = input("Ingrese una palabra: ")
x = 0
cantidad = 0

for x in palabra:
    if x in vocales:
        cantidad= cantidad + 1
print(f"La cantidad de vocales es {cantidad}")

