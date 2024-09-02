# Programa para buscar un valor en una matriz bidimensional

def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz."

# Matriz bidimensional 3x3
matriz = [
    [5, 8, 12],
    [9, 3, 7],
    [14, 6, 1]
]

# Valor a buscar
valor_a_buscar = int(input("Ingresa el valor a buscar en la matriz: "))

# Llamada a la función de búsqueda
resultado = buscar_en_matriz(matriz, valor_a_buscar)

# Mostrar el resultado
print(resultado)
