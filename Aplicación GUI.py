#Beltrán Semana 13 _ Aplicación GUI

import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI Básica")  # Establece el título de la ventana principal

# Función que agrega un dato a la lista
def agregar_dato():
    """
    Esta función obtiene el dato ingresado en el campo de texto (entry_dato),
    lo agrega a la lista (listbox_datos) y luego limpia el campo de texto.
    Si el campo de texto está vacío, muestra una advertencia.
    """
    dato = entry_dato.get()  # Obtiene el texto ingresado en el campo de texto
    if dato != "":  # Si el campo no está vacío
        listbox_datos.insert(tk.END, dato)  # Agrega el dato a la lista
        entry_dato.delete(0, tk.END)  # Limpia el campo de texto
    else:
        # Si el campo está vacío, se mostrará una advertencia
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dato.")

# Función para limpiar los datos de la lista
def limpiar_datos():
    """
    Esta función limpia la lista de datos (listbox_datos).
    """
    listbox_datos.delete(0, tk.END)  # Elimina todos los elementos de la lista

# Diseño de la interfaz

# Etiqueta que indica al usuario que ingrese un dato
label_dato = tk.Label(root, text="Ingresa un dato:")
label_dato.pack(pady=10)  # Empaqueta la etiqueta en la ventana con un espacio de 10px de margen

# Campo de texto para ingresar un dato
entry_dato = tk.Entry(root, width=40)  # Crea un campo de texto de 40 caracteres de ancho
entry_dato.pack(pady=5)  # Empaqueta el campo de texto con un margen de 5px

# Botón para agregar un dato a la lista
boton_agregar = tk.Button(root, text="Agregar", command=agregar_dato)  # Asocia el botón a la función agregar_dato
boton_agregar.pack(pady=5)  # Empaqueta el botón con un margen de 5px

# Lista donde se mostrarán los datos agregados
listbox_datos = tk.Listbox(root, width=40, height=10)  # Crea una lista con 40 caracteres de ancho y 10 filas visibles
listbox_datos.pack(pady=10)  # Empaqueta la lista con un margen de 10px

# Botón para limpiar la lista de datos
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_datos)  # Asocia el botón a la función limpiar_datos
boton_limpiar.pack(pady=5)  # Empaqueta el botón con un margen de 5px

# Ejecutar la ventana
root.mainloop()  # Inicia el bucle de eventos para que la ventana permanezca abierta
