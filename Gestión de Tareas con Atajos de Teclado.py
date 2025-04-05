#Beltrán Semana 16_Tarea: Manejadores de eventos

import tkinter as tk
from tkinter import messagebox

# Clase principal de la aplicación
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")  # Título de la ventana
        self.root.geometry("400x400")        # Tamaño de la ventana

        self.tasks = []  # Lista para almacenar las tareas como diccionarios {"text": ..., "completed": ...}

        # ======= Campo de entrada para escribir las nuevas tareas =======
        self.entry = tk.Entry(root, width=40)  # Entrada de texto con ancho 40 caracteres
        self.entry.pack(pady=10)               # Posicionar con margen vertical
        self.entry.focus()                     # Colocar el foco automáticamente en el campo

        # ======= Botones: Añadir, Completar, Eliminar =======
        btn_frame = tk.Frame(root)             # Crear un contenedor para organizar los botones
        btn_frame.pack(pady=5)

        # Botón para añadir tareas
        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        # Botón para marcar la tarea como completada
        self.complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        # Botón para eliminar las tareas
        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # ======= Lista para mostrar las tareas =======
        self.task_listbox = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # ======= Atajos de teclado =======
        self.entry.bind("<Return>", lambda event: self.add_task())        # Añadir tarea con tecla Enter
        self.root.bind("<c>", lambda event: self.complete_task())         # Marcar tarea con tecla 'c'
        self.root.bind("<C>", lambda event: self.complete_task())         # También con mayúscula 'C'
        self.root.bind("<d>", lambda event: self.delete_task())           # Eliminar tarea con 'd'
        self.root.bind("<D>", lambda event: self.delete_task())           # También con mayúscula 'D'
        self.root.bind("<Delete>", lambda event: self.delete_task())      # Eliminar con tecla 'Delete'
        self.root.bind("<Escape>", lambda event: self.root.destroy())     # Cerrar app con tecla 'Escape'

    # ======= Función para añadir tarea =======
    def add_task(self):
        task_text = self.entry.get().strip()     # Obtener texto del campo y quitar espacios
        if task_text:
            # Agregar nueva tarea como no completada
            self.tasks.append({"text": task_text, "completed": False})
            self.entry.delete(0, tk.END)         # Limpiar el campo de entrada
            self.update_task_list()              # Actualizar la lista mostrada
        else:
            # Mostrar advertencia si el campo está vacío
            messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea.")

    # ======= Función para marcar tarea como completada/incompleta =======
    def complete_task(self):
        selected = self.task_listbox.curselection()  # Obtener el índice de la tarea seleccionada
        if selected:
            index = selected[0]
            # Invertir el estado de completado (True <-> False)
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()

    # ======= función para eliminar una tarea seleccionada =======
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]         # Eliminar del listado de las tareas
            self.update_task_list()

    # ======= Función para actualizar la lista visual de tareas =======
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)  # Limpiar la lista actual en pantalla
        for task in self.tasks:
            display_text = task["text"]
            if task["completed"]:
                display_text += " ✅"        # Añadir check si la tarea ya está completada
            self.task_listbox.insert(tk.END, display_text)  # Mostrar la tarea

# ======= Ejecutar la aplicación =======
if __name__ == "__main__":
    root = tk.Tk()                # Crear la ventana principal
    app = TaskManagerApp(root)    # Crear una instancia de la aplicación GUI
    root.mainloop()               # Iniciar el bucle principal de la aplicación
