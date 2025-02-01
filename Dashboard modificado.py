#Código modificado para la tarea de la semana 8_Beltrán

import os

def mostrar_menu():
    """Muestra el menú principal de selección de unidad"""
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    """Muestra las subcarpetas (semanas) dentro de cada unidad"""
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta (Semana)")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_tareas(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_tareas(ruta_sub_carpeta):
    """Muestra las tareas (archivos) dentro de cada semana (subcarpeta)"""
    tareas = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file()]

    if not tareas:
        print(f"\nNo hay tareas en {ruta_sub_carpeta}.")
    else:
        while True:
            print("\nTareas - Selecciona una tarea")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i} - {tarea}")
            print("0 - Regresar al submenú anterior")
            print("9 - Regresar al menú principal")

            eleccion_tarea = input("Elige una tarea, '0' para regresar o '9' para ir al menú principal: ")
            if eleccion_tarea == '0':
                break
            elif eleccion_tarea == '9':
                return
            else:
                try:
                    eleccion_tarea = int(eleccion_tarea) - 1
                    if 0 <= eleccion_tarea < len(tareas):
                        print(f"Seleccionaste la tarea: {tareas[eleccion_tarea]}")
                        input("\nPresiona Enter para volver al menú de tareas.")
                    else:
                        print("Opción no válida. Por favor, intenta de nuevo.")
                except ValueError:
                    print("Opción no válida. Por favor, intenta de nuevo.")

def crear_estructura():
    """Crea la estructura de carpetas vacías para las unidades y semanas"""
    ruta_base = os.path.dirname(__file__)
    
    # Definir las unidades y semanas
    unidades = ['Unidad 1', 'Unidad 2']
    semanas = [f'Semana {i}' for i in range(1, 9)]

    for unidad in unidades:
        ruta_unidad = os.path.join(ruta_base, unidad)
        if not os.path.exists(ruta_unidad):
            os.mkdir(ruta_unidad)
        
        for semana in semanas:
            ruta_semana = os.path.join(ruta_unidad, semana)
            if not os.path.exists(ruta_semana):
                os.mkdir(ruta_semana)
    
    print("Estructura de carpetas creada exitosamente.")

# Ejecutar la creación de la estructura solo una vez
if __name__ == "__main__":
    # Descomentar para crear la estructura de carpetas vacías
    # crear_estructura()
    
    mostrar_menu()
