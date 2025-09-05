import tkinter as tk

class Participante:
    def __init__(self, nombre, institucion):
        super().__init__()
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        pass

class BandaEscolar(Participante):

    def __init__(self, nombre, institucion, categoria, total, promedio):
        super().__init__(nombre, institucion)
        self._categoria = categoria
        self._puntajes = {}
        self.categorias = ["primaria","básico","diversificado"]
        self.criterios = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]
        self.__total = total
        self.__promedio = promedio

    def set_categoria(self, categoria):
        if categoria not in self.categorias:
            raise ValueError(f"La categoria {categoria} no existe")
        self._categoria = categoria

    def registrar_puntajes(self, puntajes):
        puntajes_completos = {}
        for crit in self.criterios:
            puntajes_completos[crit] = 0

        for crit, val in puntajes.items():
            if crit not in self.criterios:
                raise ValueError(f"Criterio no válido: {crit}")
            if not (0 <= val <= 10):
                raise ValueError(f"Puntaje inválido en {crit}: {val}")
            puntajes_completos[crit] = val

        self._puntajes = puntajes_completos

    @property
    def total(self):
        return sum(self._puntajes.values())

    @property
    def promedio(self):
        return self.total / len(self._puntajes)

    def mostrar_info(self):
        return f"{self.nombre} | {self.institucion} - Categoria: {self.categoria} - Puntaje: {self.puntajes}"

def inscribir_banda():
    print("Se abrió la ventana: Inscribir Banda")
    ventana_inscribir = tk.Toplevel(ventana)
    ventana_inscribir.title("Inscribir Banda")
    ventana_inscribir.geometry("400x300")

def registrar_evaluacion():
    print("Se abrió la ventana: Registrar Evaluación")
    ventana_eval = tk.Toplevel(ventana)
    ventana_eval.title("Registrar Evaluación")
    ventana_eval.geometry("400x300")

def listar_bandas():
    print("Se abrió la ventana: Listado de Bandas")
    ventana_listado = tk.Toplevel(ventana)
    ventana_listado.title("Listado de Bandas")
    ventana_listado.geometry("400x300")

def ver_ranking():
    print("Se abrió la ventana: Ranking Final")
    ventana_ranking = tk.Toplevel(ventana)
    ventana_ranking.title("Ranking Final")
    ventana_ranking.geometry("400x300")

def salir():
    print("Aplicación cerrada")
    ventana.quit()

ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x150")

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
