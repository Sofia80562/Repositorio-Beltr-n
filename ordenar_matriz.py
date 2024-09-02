# Programa para ordenar una fila específica en una matriz bidimensional

def ordenar_fila(matriz, fila_index):
    # Implementación del algoritmo de Bubble Sort para ordenar la fila
    fila = matriz[fila_index]
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

    matriz[fila_index] = fila

# Matriz bidimensional 3x3
matriz = [
    [5, 8, 12],
    [9, 3, 7],
    [14, 6, 1]
]

# Fila a ordenar
fila_index = int(input("Ingresa el índice de la fila a ordenar (0-2): "))

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Llamada a la función de ordenación
ordenar_fila(matriz, fila_index)

# Mostrar matriz con la fila ordenada
print(f"\nMatriz después de ordenar la fila {fila_index}:")
for fila in matriz:
    print(fila)
