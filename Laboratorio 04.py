import tkinter as tk
from tkinter import messagebox

def inscribir_banda():
    messagebox.showinfo("Inscripción", "Aquí se inscribiría una banda")

def registrar_evaluacion():
    messagebox.showinfo("Evaluación", "Aquí se registrarían los puntajes")

def listar_bandas():
    messagebox.showinfo("Listado", "Aquí se mostraría el listado de bandas")

def ver_ranking():
    messagebox.showinfo("Ranking", "Aquí se mostraría el ranking final")

def salir():
    ventana.quit()

ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x300")

barra_menu = tk.Menu(ventana)

menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Inscribir Banda", command=inscribir_banda)
menu_opciones.add_command(label="Registrar Evaluación", command=registrar_evaluacion)
menu_opciones.add_command(label="Listar Bandas", command=listar_bandas)
menu_opciones.add_command(label="Ver Ranking", command=ver_ranking)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

ventana.config(menu=barra_menu)

etiqueta = tk.Label(
    ventana,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 12, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)

ventana.mainloop()
