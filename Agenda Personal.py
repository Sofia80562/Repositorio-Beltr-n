import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame para entrada de datos
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(frame_input, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1)

        tk.Label(frame_input, text="Hora:").grid(row=1, column=0)
        self.time_entry = tk.Entry(frame_input)
        self.time_entry.grid(row=1, column=1)

        tk.Label(frame_input, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(frame_input, width=30)
        self.desc_entry.grid(row=2, column=1)

        # Botones
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        btn_add = tk.Button(frame_buttons, text="Agregar Evento", command=self.add_event)
        btn_add.grid(row=0, column=0, padx=5)

        btn_delete = tk.Button(frame_buttons, text="Eliminar Evento", command=self.delete_event)
        btn_delete.grid(row=0, column=1, padx=5)

        btn_exit = tk.Button(frame_buttons, text="Salir", command=self.root.quit)
        btn_exit.grid(row=0, column=2, padx=5)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        if date and time and desc:
            self.tree.insert("", "end", values=(date, time, desc))
            self.clear_entries()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            if messagebox.askyesno("Confirmación", "¿Seguro que deseas eliminar el evento?"):
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

    def clear_entries(self):
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
