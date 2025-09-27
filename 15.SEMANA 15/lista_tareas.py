import tkinter as tk
from tkinter import messagebox
from gui import setup_ui  # Importa función para crear interfaz
from logic import TaskManager  # Importa clase para lógica de tareas


class ListaTareas:
    """
    Clase POO principal: Integra GUI y lógica de tareas.
    Usa TaskManager para datos y métodos de tareas.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas - GUI Simple")
        self.root.geometry("350x400")

        # Instancia lógica de tareas
        self.task_manager = TaskManager()

        # Crea interfaz y obtiene widgets
        self.task_entry, self.task_listbox = setup_ui(self.root, self)

        # Bind para evento de teclado: Enter añade tarea
        self.task_entry.bind('<Return>', lambda e: self.add_task())

        # Evento opcional: Doble clic para toggle completada
        self.task_listbox.bind('<Double-1>', lambda e: self.toggle_complete())

    def add_task(self):
        """Llama a lógica para añadir tarea."""
        self.task_manager.add_task(self.task_entry, self.task_listbox)

    def toggle_complete(self):
        """Llama a lógica para toggle completada."""
        self.task_manager.toggle_complete(self.task_listbox, self.task_manager.tasks)

    def delete_task(self):
        """Llama a lógica para eliminar tarea."""
        self.task_manager.delete_task(self.task_listbox, self.task_manager.tasks)