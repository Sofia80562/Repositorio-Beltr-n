# Archivos de Texto Semana 16

# Creamos un nuevo archivo llamado my_notes.txt

with open('my_notes.txt', 'w') as file:

# Escribimos notas personales en el archivo

    file.write("Nota 1: Practicar el canto.\n")
    file.write("Nota 2: Escuchar música.\n")
    file.write("Nota 3: Dibujar.\n")


# Abrimos el archivo my_notes.txt para leer

with open('my_notes.txt', 'r') as file:

    # Leemos el contenido del archivo línea por línea

    for line in file:
        # Mostramos en la consola cada línea leída

        print(line.strip())  # strip() elimina espacios en blanco y saltos de línea


