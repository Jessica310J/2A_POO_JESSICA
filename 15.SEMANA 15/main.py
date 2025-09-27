import tkinter as tk
from lista_tareas import ListaTareas

def main():
    """Crea la ventana raíz y lanza la app ListaTareas con bucle de eventos."""
    root = tk.Tk()
    app = ListaTareas(root)
    root.mainloop()

if __name__ == "__main__":
    main()