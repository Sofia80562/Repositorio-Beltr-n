#Beltrán_Semana 15 Tarea

import tkinter as tk
from tkinter import messagebox

# Se añade una función para añadir una tarea a la lista
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)  # Agrega la tarea al final de la lista
        task_entry.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

# Añadir función para marcar una tarea como completada
def mark_completed():
    try:
        selected_index = tasks_listbox.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        task_text = tasks_listbox.get(selected_index)
        if not task_text.startswith("✔ "):
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, f"✔ {task_text}")  # Agrega el prefijo de tarea completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

# Se añade función para eliminar una tarea de la lista
def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]  # Obtiene el índice de la tarea seleccionada
        tasks_listbox.delete(selected_index)  # Elimina la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

# Una función para añadir una tarea al presionar Enter
def on_enter_pressed(event):
    add_task()

# Una configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x300")

# Campo de entrada de tareas
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", on_enter_pressed)  # Vincula la tecla Enter para añadir tareas

# Marco para organizar los botones
btn_frame = tk.Frame(root)
btn_frame.pack()

# Añadimos un botón para añadir una tarea
task_add_button = tk.Button(btn_frame, text="Añadir Tarea", command=add_task)
task_add_button.pack(side=tk.LEFT, padx=5)

# Añadimos un botón para marcar una tarea como completada
task_complete_button = tk.Button(btn_frame, text="Marcar como Completada", command=mark_completed)
task_complete_button.pack(side=tk.LEFT, padx=5)

# Se añade un botón para eliminar una tarea
task_delete_button = tk.Button(btn_frame, text="Eliminar Tarea", command=delete_task)
task_delete_button.pack(side=tk.LEFT, padx=5)

# Lista de tareas
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

# Ejecutar la aplicación :D
root.mainloop()
