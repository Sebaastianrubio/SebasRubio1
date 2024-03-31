print("UNIVERSIDAD ESTATAL AMAZONICA")
#calcualdora
nombre=input("ingrese el nombre del cliente:")
cantidad=input("Inngresa la cantidad de celulares comprados:")
valor=input(input("ingrese el costo del celular:"))

#Desarrollo
montoTotal = cantidad * valor

descuento = (montoTotal * 10) /100

Total_Pago = montoTotal-descuento

#Salidas
print(nombre,'sebastian Usted compro',cantidad,'2 celulares')
print('300 valor sin Descuento es:',montoTotal)
print('Descuento del 10%:',descuento)
print('Usted debe Pagar con descuento:',Total_Pago)

