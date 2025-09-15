# main.py

import tkinter as tk
from gui import AgendaGUI  # Importa la clase que crea la interfaz

def main():
    root = tk.Tk()          # Crea ventana principal
    app = AgendaGUI(root)   # Instancia la interfaz
    root.mainloop()         # Ejecuta el loop principal de eventos

if __name__ == "__main__":
    main()  # Ejecuta la aplicación