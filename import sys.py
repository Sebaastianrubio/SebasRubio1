import sys
while True:
    print("********Universiddad Estatal Amazonica**********")
    eleccion = input("""
1 - Declare 6 variables unidimensionales y asigne valores enteros
2 - Declare 6 variables unidimensionales y asigne valores flotantes
3 - Declare 6 variables unidimensionales y asignar valores de texto
4 - Declare 6 variables unidimensionales y asignar valores de enteros, flotantes y texto
5 - Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores enteros (6 variables en total)

Seleccione La Opcion: """)
    if eleccion == "1":
        for n in [3, 2, 5, 1, 5, 4]:
            print("El arreglo es:",n)
    elif eleccion == "2":
        for p in [3.2, 2.5, 5.9, 1.8, 5.3, 4.36]:
             print("El arreglo es:",p)
    elif eleccion == "3":
        for i in ['GUAYAS', 'LOS RIOS', 'CHIMBORAZO', 'ESMERALDAS', 'PICHINCHA', 'AZUAY']:
            print("El arreglo es:", i)
    elif eleccion == "4":
        for j in [100, 693, 315.65, 698.19, 'Tena', 'Puyo' ]:
            print("El arreglo es:", j)
    elif eleccion == "5":
        matriz = np.array([[1, 2, 3], [4, 5, 6]])
        print(matriz)
    