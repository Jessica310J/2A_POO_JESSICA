# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from utils import validar_hora  # Importa función para validar hora

class AgendaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")  # Título ventana
        self.root.geometry("550x350")       # Tamaño ventana

        # Frame para contener la lista de eventos
        frame_lista = ttk.Frame(root)
        frame_lista.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # TreeView para mostrar eventos con columnas Fecha, Hora y Descripción
        cols = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=cols, show="headings", height=10)
        for c in cols:
            self.tree.heading(c, text=c)  # Títulos columnas
        self.tree.column("Fecha", width=100, anchor=tk.CENTER)  # Ancho y alineación
        self.tree.column("Hora", width=80, anchor=tk.CENTER)
        self.tree.column("Descripción", width=340, anchor=tk.W)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar vertical para el TreeView
        scroll = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame para los campos de entrada
        frame_entrada = ttk.Frame(root)
        frame_entrada.pack(padx=10, pady=5, fill=tk.X)

        # Campo Fecha con DateEntry (calendario desplegable)
        ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Campo Hora (texto)
        ttk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_hora = ttk.Entry(frame_entrada, width=10)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)

        # Campo Descripción (texto)
        ttk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_desc = ttk.Entry(frame_entrada, width=50)
        self.entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Frame para botones
        frame_botones = ttk.Frame(root)
        frame_botones.pack(padx=10, pady=5, fill=tk.X)

        # Botón para agregar evento
        btn_agregar = ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar evento seleccionado
        btn_eliminar = ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Botón para salir de la aplicación
        btn_salir = ttk.Button(frame_botones, text="Salir", command=root.quit)
        btn_salir.pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()  # Obtiene fecha seleccionada
        hora = self.entry_hora.get().strip()  # Obtiene hora ingresada
        desc = self.entry_desc.get().strip()  # Obtiene descripción

        # Verifica que hora y descripción no estén vacíos
        if not hora or not desc:
            messagebox.showwarning("Campos vacíos", "Complete todos los campos.")
            return
        # Valida formato de hora
        if not validar_hora(hora):
            messagebox.showerror("Hora inválida", "Formato de hora debe ser HH:MM (24h).")
            return

        # Inserta nuevo evento en el TreeView
        self.tree.insert("", "end", values=(fecha, hora, desc))

        # Limpia campos hora y descripción para nueva entrada
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()  # Obtiene evento seleccionado
        if not seleccionado:
            messagebox.showinfo("Sin selección", "Seleccione un evento para eliminar.")
            return
        # Pregunta confirmación antes de eliminar
        if messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?"):
            for item in seleccionado:
                self.tree.delete(item)  # Elimina evento del TreeView