import random

intentosrealizados=0
nunMinimo= 1
nunMax= 20

print('Hola Como te Llamas')
nombre=input()

numero=random.randint(nunMinimo,nunMax)  # Funcion para Generar un NUmero Aleatorio Entero
print ('Bienvenido' + nombre + ' Ingresa un  numero entre: ' + str(nunMinimo) + 'and' + str(nunMax))

while intentosrealizados < 6:
     print("Intenta adivinar: ")
     estimacion= input()
     estimacion= int(estimacion)

     intentosrealizados = intentosrealizados+1

     if estimacion < numero:    # Aqui validamos si el numero es menor al que da la Computadora
          print(" Tu Numero es Demasiado Bajo")
          if estimacion > numero:
               print(" Tu numero es demasiado Alto")
               if estimacion == numero:
break
 print("Buen Trabajo" + nombre)

