from tkinter import messagebox
import tkinter as tk


class TaskManager:
    """
    Clase POO para manejar lógica de tareas (datos y operaciones).
    Independiente de GUI: Puede usarse para pruebas sin ventana.
    Atributos: self.tasks (lista de strings con [ ] o [X]).
    """

    def __init__(self):
        self.tasks = []  # Lista interna para tareas

    def add_task(self, task_entry, task_listbox):
        """Añade tarea: Valida input, agrega con prefijo [ ] y actualiza Listbox."""
        text = task_entry.get().strip()
        if not text:
            messagebox.showwarning("Error", "Ingresa una tarea.")
            return

        task = f"[ ] {text}"
        self.tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

    def toggle_complete(self, task_listbox, tasks):
        """Toggle estado de tarea: Cambia [ ] a [X] o viceversa (cambio visual)."""
        sel = task_listbox.curselection()
        if not sel:
            messagebox.showwarning("Error", "Selecciona una tarea.")
            return

        idx = sel[0]
        task = tasks[idx]

        if task.startswith("[X] "):
            new_task = f"[ ] {task[4:]}"
        else:
            new_task = f"[X] {task[3:]}"

        tasks[idx] = new_task
        task_listbox.delete(idx)
        task_listbox.insert(idx, new_task)
        task_listbox.selection_clear(0, tk.END)

    def delete_task(self, task_listbox, tasks):
        """Elimina tarea seleccionada con confirmación."""
        sel = task_listbox.curselection()
        if not sel:
            messagebox.showwarning("Error", "Selecciona una tarea.")
            return

        idx = sel[0]
        if messagebox.askyesno("Confirmar", "¿Eliminar?"):
            del tasks[idx]
            task_listbox.delete(idx)