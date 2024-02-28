
# Programa para buscar un elemento en una matriz de 3 x 3

matriz = [[11, 2, 3],[8, 7, 5],[9, 10, 1]]
print("La Matriz es: \n")
for fila in range(0, len(matriz)):
    print(matriz[fila])
    for columna in range(0, len(matriz[fila])):
        elemento = matriz[fila][columna]
        if elemento == 1:
            print("¡El numero fue encontrado!")
            coordenadaX = columna + 1
            coordenadaY = fila + 1
            print(f"La coordenda del numero es: ({coordenadaX}, {coordenadaY})")