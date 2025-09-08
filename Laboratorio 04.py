import tkinter as tk
from tkinter import ttk, messagebox

class Participante:
    def __init__(self, nombre, institucion):
        super().__init__()
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        pass

class BandaEscolar(Participante):

    def __init__(self, nombre, institucion, categoria):
        super().__init__(nombre, institucion)
        self._categoria = categoria
        self._puntajes = {}
        self.categorias = ["primaria","básico","diversificado"]
        self.criterios = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]

    @property
    def categoria(self):
        return self._categoria

    @property
    def puntajes(self):
        return self._puntajes

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

class Concurso:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.bandas = {}

    def inscribir_banda(self, banda: BandaEscolar):
        if banda.nombre in self.bandas:
            raise ValueError(f"La banda {banda.nombre} ya está inscrita")
        self.bandas[banda.nombre] = banda

    def registrar_evaluacion(self, nombre_banda, puntajes):
        if nombre_banda not in self.bandas:
            raise ValueError(f"La banda {nombre_banda} no está inscrita")
        self.bandas[nombre_banda].registrar_puntajes(puntajes)

    def listar_bandas(self):
        return [banda.mostrar_info() for banda in self.bandas.values()]

    def ranking(self):
        return sorted(
            self.bandas.values(),
            key=lambda b: (
                -b.total,
                -b.puntajes.get("ritmo", 0),
                -b.puntajes.get("uniformidad", 0),
                -b.puntajes.get("coreografía", 0),
                -b.puntajes.get("alineación", 0),
                -b.puntajes.get("puntualidad", 0),
                b.nombre
            )
        )

class ConcursoBandasApp:
    def __init__(self):
        self.concurso = Concurso("Concurso de Bandas", "14/09/2025")
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("600x150")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Inscribir Banda")
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=0, column=1, padx=6, pady=6)

        tk.Label(ventana, text="Institución:").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        entry_institucion = tk.Entry(ventana)
        entry_institucion.grid(row=1, column=1, padx=6, pady=6)

        tk.Label(ventana, text="Categoría:").grid(row=2, column=0, padx=6, pady=6, sticky="w")
        combo_categoria = ttk.Combobox(ventana, values=["primaria", "básico", "diversificado"], state="readonly")
        combo_categoria.grid(row=2, column=1, padx=6, pady=6)
        combo_categoria.set("primaria")

        def guardar():
            try:
                nombre = entry_nombre.get().strip()
                institucion = entry_institucion.get().strip()
                categoria = combo_categoria.get().lower()
                if not nombre or not institucion:
                    raise ValueError("Nombre e institución son obligatorios.")
                banda = BandaEscolar(nombre, institucion, categoria)
                self.concurso.inscribir_banda(banda)
                tk.messagebox.showinfo("Éxito", f"Banda '{nombre}' inscrita correctamente")
                ventana.destroy()
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

        tk.Button(ventana, text="Guardar", command=guardar).grid(row=3, column=0, columnspan=2, pady=10)

    def registrar_evaluacion(self):
        if not self.concurso.bandas:
            tk.messagebox.showinfo("Aviso", "Aún no hay bandas inscritas.")
            return

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registrar Evaluación")

        tk.Label(ventana, text="Seleccione Banda:").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        combo_banda = ttk.Combobox(ventana, values=list(self.concurso.bandas.keys()), state="readonly")
        combo_banda.grid(row=0, column=1, padx=6, pady=6)
        combo_banda.set(list(self.concurso.bandas.keys())[0])

        entries = {}
        criterios = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]
        for i, crit in enumerate(criterios, start=1):
            tk.Label(ventana, text=f"{crit.capitalize()} (0-10):").grid(row=i, column=0, padx=6, pady=4, sticky="w")
            entry = tk.Spinbox(ventana, from_=0, to=10, width=5)
            entry.delete(0, "end")
            entry.insert(0, "0")
            entry.grid(row=i, column=1, padx=6, pady=4)
            entries[crit] = entry

        def guardar():
            try:
                banda = combo_banda.get()
                puntajes = {crit: int(entry.get()) for crit, entry in entries.items()}
                self.concurso.registrar_evaluacion(banda, puntajes)
                tk.messagebox.showinfo("Éxito", f"Evaluación registrada para {banda}")
                ventana.destroy()
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

        tk.Button(ventana, text="Guardar Evaluación", command=guardar).grid(row=len(criterios) + 1, column=0,
                                                                            columnspan=2, pady=10)

    def listar_bandas(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Listado de Bandas")

        tree = ttk.Treeview(ventana, columns=("Nombre", "Institución", "Categoría", "Total", "Promedio"),
                            show="headings")
        for col in ("Nombre", "Institución", "Categoría", "Total", "Promedio"):
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor="center")
        tree.pack(fill="both", expand=True)

        for banda in self.concurso.bandas.values():
            tree.insert("", "end", values=(banda.nombre, banda.institucion, banda.categoria, banda.total,
                                           round(banda.promedio, 2)))

    def ver_ranking(self):
        if not self.concurso.bandas:
            tk.messagebox.showinfo("Aviso", "No hay bandas inscritas.")
            return

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Ranking")

        tree = ttk.Treeview(ventana, columns=("Posición", "Nombre", "Institución", "Categoría", "Total", "Promedio"),show="headings")

        for col in ("Posición", "Nombre", "Institución", "Categoría", "Total", "Promedio"):
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        tree.pack(fill="both", expand=True)

        ranking = self.concurso.ranking()
        for i, banda in enumerate(ranking, start=1):
            tree.insert("","end",values=(i, banda.nombre, banda.institucion, banda.categoria, banda.total, round(banda.promedio, 2)))

if __name__ == "__main__":
    ConcursoBandasApp()