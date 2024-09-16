# Función para calcular la temperatura promedio de una ciudad
def promedio_temperatura_ciudad(temperaturas, ciudad):
    """
    Calcular el promedio de las temperaturas de una ciudad específica.

    :param temperaturas: Lista de temperaturas [ciudad][semana][día]
    :param ciudad: Índice de la ciudad (0 = Quito, 1 = Guayaquil, 2 = Cuenca)
    :return: El promedio de la temperatura de la ciudad
    """
    total_temperatura = 0
    total_dias = 0

    # Recorremos las semanas y los días de la ciudad seleccionada
    for semana in temperaturas[ciudad]:
        for dia in semana:
            total_temperatura += dia
            total_dias += 1

    # Calculamos el promedio
    promedio = total_temperatura / total_dias if total_dias > 0 else 0
    return promedio


# Datos de las temperaturas (tomando como base la tarea anterior)
temperaturas = [
    # Quito
    [
        # Semana 1
        [15, 16, 14, 17, 16, 15, 14],
        # Semana 2
        [17, 18, 16, 17, 16, 17, 18]
    ],
    # Guayaquil
    [
        # Semana 1
        [28, 29, 30, 31, 29, 28, 30],
        # Semana 2
        [30, 31, 32, 33, 31, 30, 32]
    ],
    # Cuenca
    [
        # Semana 1
        [12, 14, 13, 15, 14, 12, 13],
        # Semana 2
        [13, 15, 14, 16, 15, 14, 13]
    ]
]

# Cálculo de la temperatura promedio para cada ciudad
ciudades = ['Quito', 'Guayaquil', 'Cuenca']

for i, ciudad in enumerate(ciudades):
    promedio = promedio_temperatura_ciudad(temperaturas, i)
    print(f"Temperatura promedio de {ciudad}: {promedio:.2f}°C")


