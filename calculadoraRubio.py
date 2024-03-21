
import math
import os
#Aquí importamos las librerías

def Menu():  #Aquí definimos una pequeña funcion para hacer el menu
 
    print("                       -                      UNIVERSIDAD ESTATAL AMAZONICA                     -")
    print("                       º                      :: C A L C U L A D O R A::                        º")
    print("                       --------------------------------------------------------------------------")
    print("                       º                                                                        º")
    print("                       º  1.- Suma        2.- Resta       3.-Multiplicación      4.- División   º")
    print("                       º                                                                        º")
    print("                       º  5.- Potencia    6.- Raíz Cudrada     7.- M.C.M         8.- M.C.D      º")
    print("                       º                                                                        º")
    print("                       º  9.- Fibonacci  10.- Factorial        11.- Menu         12.- Salir     º")                                                                
    print("                       º                                                                        º")
    print("                       º                                                                        º")
    print("                       º                                                                        º")
    print("                       --------------------------------------------------------------------------")
    print("")
 
def mcd(num1, num2):          #Aquí definimos una funcion para el maximo comun divisor 
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd
 
def mcm(num1, num2):        #Aquí definimos una funcion para el minimo comun multiplo 
    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd(a, b)) * b
    return mcm
 
def borrarPantalla():       #Aquí definimos una funcion para borrar la pantalla
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
 
def Calculadora():         #Aquí definimos una funcion donde tenemos las disntitas operaciones
 
    Menu()
 
    opc = int(input("Selecione nº de Opción: "))
 
    while (opc >0 and opc <13):              #Aquí validamos mientras las opciones esten ese rango entramos
 
        if (opc==1):
            print("")                       
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Suma es:', num1+num2)        #Aquí realizamos la suma operador aritmetico 
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":          #Aquí validamos la opcion operadores logicos 
                opc = 1
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 1
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
 
        elif(opc==2):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Resta es:',num1-num2)                #Aquí realizamos la resta operador aritmetico 
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 2
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 2
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==3):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print ('La Multiplicacion es:', num1*num2)            #Aquí realizamos la multiplicacion 
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 3
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 3
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==4):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
 
            try:
              print ('La Division es:', num1/num2)          #Aquí realizamos la division 
              print("")
              Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
              if Continuar == "s" or Continuar == "S":
                opc = 4
 
              elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
              else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 4
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
            except ZeroDivisionError:                        #Aquí condicionamos que division para cero no existe 
              print ('No se Permite la Division Entre 0')
              print("")
              Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
              if Continuar == "s" or Continuar == "S":
                opc = 4
 
              elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
              else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 4
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==5):
            print("")
            base = int(input("Ingrese Base: "))
            print("")
            exponente = int(input("Ingrese Exponente: "))
            print("")
            print('La Potencia es:', base**exponente)           #Aquí realizamos la potencia elevadada de un numero 
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 5
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 5
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==6):
            print("")
            num = int(input("Ingrese Número: "))
            print("")
            print("La raíz cuadrada de {} es {}".format(num, math.sqrt(num)))   #Aquí realizamos la raiz cuadrada con la funcion sqrt
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 6
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("SSelecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 6
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
       
 
        elif(opc==7):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print("El M.C.M. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcm(num1, num2)))  #Aquí realizamos el MCM
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 7
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 7
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==8):
            print("")
            num1 = int(input("Ingrese Primer Número: "))
            print("")
            num2 = int(input("Ingrese Segundo Número: "))
            print("")
            print("El M.C.D. entre "+str(num1)+" y "+str(num2)+" es: "+str(mcd(num1, num2)))                   #Aquí realizamos el MCD
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 8
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 8
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==9):
            print("")
            fibonacci = []
            x = 0
            y = 1
            num = int(input("Numero de elementos: "))           #Aquí realizamos la serie del Fibonacci con la funcion fibonacci
            print("")
            for n in range(num):
                fibonacci.append(x + y)
                aux = x + y
                x = y
                y = aux
            print(fibonacci)
            print("")
            Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
            if Continuar == "s" or Continuar == "S":
                opc = 9
 
            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione nº de Opción: "))
 
            else:
                print("")
                Continuar = input("Por Favor escoja(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 9
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==10):
            print("")
            num = int(input("Ingrese Número: "))
            print("")
            try:
                print("El factorial de {} es {}".format(num, math.factorial(num)))            #Aquí realizamos la funcion factorial 
                print("")
                Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 10
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("SSelecione nº de Opción: "))
 
                else:
                    print("")
                    Continuar = input("Por Favor escoja(S/N): ")
 
                    if Continuar == "s" or Continuar == "S":
                        opc = 10
 
                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))
 
            except ValueError:                                                              #Aquí realizamos una validacion Factorial de numeros negativos no existe 
                print("No se Admiten Números Negativos")
                print("")
                Continuar = input("¿Desea Continuar con esta Opción?(S/N): ")
 
                if Continuar == "s" or Continuar == "S":
                    opc = 10
 
                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("SSelecione nº de Opción: "))
 
                else:
                    print("")
                    Continuar = input("Por Favor escoja(S/N): ")
 
                    if Continuar == "s" or Continuar == "S":
                        opc = 10
 
                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione nº de Opción: "))
 
 
        elif(opc==11):
            print("")
            print("Calculadora con Funciones Basicas ")
            print(" Almuno Sebastian Rubio")
            opc = int(input("Selecione nº de Opción: "))
 
        
        elif(opc==12):
            borrarPantalla()
            Menu()
            opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==11):
            Menu()
            opc = int(input("Selecione nº de Opción: "))
 
        elif(opc==12):
            exit(0)
 
    while(opc <1 or opc >13 ):
        print("")
        print("Opción no Encontrada")
        print("")
        opc = int(input("Selecione nº de Opción: "))
 
Calculadora()
