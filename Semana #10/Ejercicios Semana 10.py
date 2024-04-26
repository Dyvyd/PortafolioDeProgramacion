#Arreglo multidimensional de 3x3

matriz = [[23, 54, 12],
          [21, 81, 14],
          [16, 20, 21]]

def recorrer_matriz(matriz):
    numero_filas = len(matriz)
    #Se recorren las las filas
    for fila in range(numero_filas):
        numero_columnas = len(matriz[fila])
        #Se recorren las columnas
        for columna in range(numero_columnas):
            elemento_en_matriz = matriz[fila][columna]
            print(f"El elemento en {fila}, {columna} es: {elemento_en_matriz}")
            matriz[fila][columna] = elemento_en_matriz * 2
            print(f"El elemento modificado en {fila}, {columna} es: {matriz[fila][columna]}")

recorrer_matriz(matriz)

fila = 1
columna = 1

elemento_central = matriz[fila][columna]

print(f"El número de la {fila}, {columna} es: {elemento_central}")

fila = 1
columna = 2

elemento_esquina = matriz[fila][columna]

print(f"El número de la {fila}, {columna} es: {elemento_esquina}")

fila = 0
columna = 2

elemento_a_cambiar = matriz[fila][columna]

print(f"El número a cambiar en {fila}, {columna} es: {elemento_a_cambiar}")

matriz[fila][columna] = 96

print(f"El número cambiado en {fila}, {columna} es: {matriz[fila][columna]}")
