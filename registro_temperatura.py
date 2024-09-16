# Datos de temperaturas para 3 ciudades de Ecuador, 7 días de la semana y 2 semanas
# Matriz 3D: [ciudad][semana][día]
temperaturas = [
    # Quito
    [
        # Semana 1 (temperaturas para lunes a domingo)
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

# Lista de nombres de ciudades para referencia
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Iteramos sobre cada ciudad
for i, ciudad in enumerate(temperaturas):
    print(f"Promedio de temperaturas para {ciudades[i]}:")

    # Iteramos sobre cada semana
    for j, semana in enumerate(ciudad):
        # Calculamos el promedio de la semana
        promedio_semanal = sum(semana) / len(semana)
        print(f"  Semana {j + 1}: {promedio_semanal:.2f}°C")

