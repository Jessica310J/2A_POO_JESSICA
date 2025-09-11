import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al presionar "Agregar"
def agregar():
    texto = entrada.get()  # Obtener texto del campo
    if texto.strip():  # Verificar que no sea vacío
        lista.insert(tk.END, texto)  # Agregar texto a la lista
        entrada.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Aviso", "El campo no puede estar vacío")  # Mostrar alerta si está vacío

# Función para limpiar lista y entrada
def limpiar():
    lista.delete(0, tk.END)  # Borrar todos los elementos de la lista
    entrada.delete(0, tk.END)  # Limpiar campo de texto

# Crear ventana principal
ventana = tk.Tk()
ventana.title("App Datos")  # Título ventana

# Etiqueta para instrucción
tk.Label(ventana, text="Ingrese dato:").pack()

# Campo para ingreso de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Botón para agregar texto a la lista
tk.Button(ventana, text="Agregar", command=agregar).pack()

# Lista para mostrar los datos agregados
lista = tk.Listbox(ventana)
lista.pack()

# Botón para limpiar lista y campo
tk.Button(ventana, text="Limpiar", command=limpiar).pack()

# Mantener ventana abierta y escuchar eventos
ventana.mainloop()
