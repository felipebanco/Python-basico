#Ejercicio 5
'''Una tienda ofrece un descuento del 15% sobre el total de la compra y el cliente
desea saber cuanto deberá pagar finalmente por su compra'''

precio=float(input("Ingrese el precio del producto: "))

descuento=precio * 0.15 #Se esta scando el 15% del producto entre 100.

precio_final = precio - descuento

print(f"El precio total del producto con el descuento es de ${precio_final:.2f}")#Redondear a dos decimales despues de la coma
