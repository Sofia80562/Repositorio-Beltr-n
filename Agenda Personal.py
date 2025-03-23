#Beltrán Tarea Semana 14 Agenda Personal

#Utilizamos Tkinter para diseñar la interfaz

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")
        
        # Evitar el cierre de la ventana con la cruz (X)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Flag para verificar si se ha agregado un evento
        self.event_added = False
        
        # Frame para la entrada de datos
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10)
        
        # Etiqueta y entrada para la fecha con DateEntry
        tk.Label(frame_input, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(frame_input, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1)
        
        # Etiqueta y entrada para la hora
        tk.Label(frame_input, text="Hora:").grid(row=1, column=0)
        self.time_entry = tk.Entry(frame_input)
        self.time_entry.grid(row=1, column=1)
        
        # Etiqueta y entrada para la descripción del evento
        tk.Label(frame_input, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(frame_input, width=30)
        self.desc_entry.grid(row=2, column=1)
        
        # Frame para los botones
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)
        
        # Botón para agregar un evento
        btn_add = tk.Button(frame_buttons, text="Agregar Evento", command=self.add_event)
        btn_add.grid(row=0, column=0, padx=5)
        
        # Botón para eliminar un evento seleccionado
        btn_delete = tk.Button(frame_buttons, text="Eliminar Evento", command=self.delete_event)
        btn_delete.grid(row=0, column=1, padx=5)
        
        # Botón para salir de la aplicación (sólo funcionará si se ha agregado un evento)
        btn_exit = tk.Button(frame_buttons, text="Salir", command=self.exit_app)
        btn_exit.grid(row=0, column=2, padx=5)
        
        # Treeview para mostrar la lista de eventos
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")  # Encabezado de la columna Fecha
        self.tree.heading("Hora", text="Hora")  # Encabezado de la columna Hora
        self.tree.heading("Descripción", text="Descripción")  # Encabezado de la columna Descripción
        self.tree.pack(pady=10)
    
    def add_event(self):
        # Obtener datos ingresados por el usuario
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()
        
        # Verificar que todos los campos estén llenos
        if date and time and desc:
            self.tree.insert("", "end", values=(date, time, desc))  # Agregar evento a la lista
            self.clear_entries()  # Limpiar campos de entrada
            self.event_added = True  # Marcar que se ha agregado un evento
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")  # Mostrar advertencia
    
    def delete_event(self):
        # Obtener el elemento seleccionado en la lista
        selected_item = self.tree.selection()
        if selected_item:
            # Confirmar la eliminación del evento
            if messagebox.askyesno("Confirmación", "¿Seguro que deseas eliminar el evento?"):
                self.tree.delete(selected_item)  # Eliminar evento de la lista
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")  # Mostrar advertencia
    
    def clear_entries(self):
        # Limpiar los campos de entrada
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
    
    def exit_app(self):
        # Verificar si se ha agregado un evento antes de salir
        if not self.event_added:
            messagebox.showwarning("Advertencia", "No se ha agregado ningún evento. No puedes salir aún.")
        else:
            self.root.quit()  # Cerrar la ventana si se ha agregado un evento
    
    def on_close(self):
        # Función para interceptar el evento de cierre de la ventana
        if messagebox.askyesno("Confirmación", "¿Seguro que deseas salir?"):
            self.root.quit()  # Cerrar la ventana si se confirma

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)  # Instancia de la aplicación
    root.mainloop()  # Ejecutar el bucle principal de Tkinter

