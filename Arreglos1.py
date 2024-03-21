import sys
import numpy as np
while True:
    print("********Universiddad Estatal Amazonica**********")
    eleccion = input("""
1 - Declare 6 variables unidimensionales y asigne valores enteros
2 - Declare 6 variables unidimensionales y asigne valores flotantes
3 - Declare 6 variables unidimensionales y asignar valores de texto
4 - Declare 6 variables unidimensionales y asignar valores de enteros, flotantes y texto
5 - Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores enteros (6 variables en total)
6 - Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asigne valores flotantes (6 variables en total)
7 - Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asignar valores de texto (6 variables en total)
8 - Declare 2 variables bidimensionales 2x3, 5x5, 3x6 y asignar valores de enteros, flotantes y texto (6 variables en total)
9 - Declare 2 variables tridimensionales 2x3x2, 5x5x5, 3x6x2 y asigne valores enteros (6 variables en total)
10 - Declare 2 variables tridimensionales 2x3x1, 5x5x2, 3x6x5 y asigne valores flotantes (6 variables en total)
11 - Declare 2 variables tridimensionales 2x3x3, 5x5x4, 3x6x1 y asignar valores de texto (6 variables en total)
12 - Declare 2 variables tridimensionales 2x3x2, 5x5x1, 3x6x2 y asignar valores de enteros, flotantes y texto (6 variables en total)
13 - Salir

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
        print(" La Matriz de 2 x 3:")
        matriz = np.array([[1, 2, 3], [4, 5, 6]])
        print(matriz)
        print(" La Matriz de 5 x 5:")
        matriz1 = np.array([[1, 2, 3, 6, 8], [4, 5, 6, 10, 99], [4, 5, 6, 10, 99], [4, 5, 6, 10, 99], [4, 5, 6, 10, 99] ])
        print(matriz1)
        print(" La Matriz de 3 x 6:")
        matriz2 = np.array( [[1, 2, 3, 6, 8, 100], [4, 5, 6, 10, 99, 1000], [4, 5, 6, 10, 99, 12]])
        print(matriz2)
    elif eleccion == "6":
        print(" La Matriz de 2 x 3:")
        matriz = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
        print(matriz)
        print(" La Matriz de 5 x 5:")
        matriz1 = np.array(
            [[1.1, 2.2, 3.2, 6.6, 8.8], [4.1, 5.2, 6.8, 10.78, 99.9], [4.8, 5.5, 6.4, 10.8, 99.9], [4.8, 5.7, 6.9, 10.8, 99.7], [4.4, 5.5, 6.8, 10.9, 99.1]])
        print(matriz1)
        print(" La Matriz de 3 x 6:")
        matriz2 = np.array([[1.1, 2.2, 3.3, 6.6, 8.8, 100.2], [4.4, 5.8, 6.7, 10.9, 99.7, 1000.4], [4.4, 5.5, 6.8, 10.9, 99.5, 12.5]])
        print(matriz2)
    elif eleccion == "7":
        print(" La Matriz de 2 x 3:")
        matriz = np.array([['GUAYAS', 'GUAYAS', 'GUAYAS'], ['Quito', 'Quito', 'Quito']])
        print(matriz)
        print(" La Matriz de 5 x 5:")
        matriz1 = np.array(
            [['Quito', 'Quito', 'Quito', 'Quito', 'Quito'], ['Paute', 'Paute', 'Paute', 'Paute', 'Paute'], ['Tena', 'Tena', 'Tena', 'Tena', 'Tena'], ['Tumbaco', 'Tumbaco', 'Tumbaco', 'Tumbaco', 'Tumbaco'], ['Tumbaco', 'Tumbaco', 'Tumbaco', 'Tumbaco', 'Tumbaco']])
        print(matriz1)
        print(" La Matriz de 3 x 6:")
        matriz2 = np.array([['a', 'b', 'c', 'd', 'f', 'g'], ['a', 'h', 'i', 'a', 'a', 'a'], ['a', 'a', 'a', 'a', 'a', 'a']])
        print(matriz2)
    elif eleccion == "8":
        print(" La Matriz de 2 x 3:")
        matriz = np.array([['GUAYAS', 1, 1.3], ['Quito', 'Quito', 8]])
        print(matriz)
        print(" La Matriz de 5 x 5:")
        matriz1 = np.array(
            [['Quito', 1, 2.1, 'Quito', 'Quito'], ['Paute', 3.3, 20000, 'Paute', 'Paute'],
             [5, 'Tena', 6.1, 'Tena', 'Tena'], ['Tumbaco', 'Tumbaco', 'Tumbaco', 'Tumbaco', 'Tumbaco'],
             ['Tumbaco', 'Tumbaco', 'Tumbaco', 'Tumbaco', 'Tumbaco']])
        print(matriz1)
        print(" La Matriz de 3 x 6:")
        matriz2 = np.array(
            [['a', 1, 'c', 'd', 4.4, 'g'], ['a', 'h', 5, 'a', 6.6, 'a'], [5, 'a', 'a', 4.5, 'a', 'a']])
        print(matriz2)
    elif eleccion == "9":
        print(" La Matriz de 2 x 3 x 2:")
        n = 2
        m = 3
        o = 2
        matriz0 = np.ones(shape=(n, m, o), dtype=int)
        print(matriz0)
        print(" La Matriz de 5 x 5 x 5:")
        n = 5
        m = 5
        o = 5
        matriz1 = np.zeros(shape=(n, m, o), dtype=int)
        print(matriz1)
        print(" La Matriz de 5 x 5 x 5:")
        n = 3
        m = 6
        o = 2
        matriz1 = np.zeros(shape=(n, m, o), dtype=int)
        print(matriz1)
    elif eleccion == "10":
        print(" La Matriz de 2 x 3 x 1:")
        arreglo_3d = [[[1.2 for x in range(2) ]for y in range(3)]for z in range(1)]
        print(arreglo_3d)
        print(" La Matriz de 5 x 5 x 2:")
        arreglo_3d = [[[1.6 for x in range(5)] for y in range(5)] for z in range(2)]
        print(arreglo_3d)
        print(" La Matriz de 3 x 6 x 5:")
        arreglo_3d = [[[1.8 for x in range(3)] for y in range(6)] for z in range(5)]
        print(arreglo_3d)
    elif eleccion == "11":
        print(" La Matriz de 2 x 3 x 3:")
        arreglo_3d = [[['Quito' for x in range(2) ]for y in range(3)]for z in range(3)]
        print(arreglo_3d)
        print(" La Matriz de 5 x 5 x 4:")
        arreglo_3d = [[['Tena' for x in range(5)] for y in range(5)] for z in range(4)]
        print(arreglo_3d)
        print(" La Matriz de 3 x 6 x 1:")
        arreglo_3d = [[['Riobamba' for x in range(3)] for y in range(6)] for z in range(1)]
        print(arreglo_3d)
    elif eleccion == "12":
        print(" La Matriz de 2 x 3 x 2:")
        arreglo_3d = [[[1 for x in range(2)] for y in range(3)] for z in range(3)]
        print(arreglo_3d)
        print(" La Matriz de 5 x 5 x 1:")
        arreglo_3d = [[[20.3 for x in range(5)] for y in range(5)] for z in range(4)]
        print(arreglo_3d)
        print(" La Matriz de 3 x 6 x 2:")
        arreglo_3d = [[['Riobamba' for x in range(3)] for y in range(6)] for z in range(1)]
        print(arreglo_3d)
    elif eleccion == "13":
        exit(0)


