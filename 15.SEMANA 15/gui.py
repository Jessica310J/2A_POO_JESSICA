import tkinter as tk


def setup_ui(root, parent):
    """
    Crea y configura la interfaz gráfica.
    Retorna: (task_entry, task_listbox) para usar en la clase principal.
    Enlaza botones a métodos de parent (e.g., parent.add_task).
    """
    # Campo de entrada
    tk.Label(root, text="Nueva Tarea:", font=("Arial", 12)).pack(pady=10)
    task_entry = tk.Entry(root, width=30)
    task_entry.pack(pady=5)
    task_entry.focus()

    # Botones para eventos de ratón (clics)
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="Añadir", command=parent.add_task, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Completar", command=parent.toggle_complete, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Eliminar", command=parent.delete_task, width=10).pack(side=tk.LEFT, padx=5)

    # Listbox con scrollbar
    list_frame = tk.Frame(root)
    list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    task_listbox = tk.Listbox(list_frame, width=40, height=15, yscrollcommand=scrollbar.set)
    task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=task_listbox.yview)

    return task_entry, task_listbox  # Retorna widgets para usar en ListaTareas