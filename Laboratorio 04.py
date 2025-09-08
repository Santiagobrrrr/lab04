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
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x150")

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
        print("Se abrió la ventana: Inscribir Banda")
        tk.Toplevel(self.ventana).title("Inscribir Banda")

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        tk.Toplevel(self.ventana).title("Registrar Evaluación")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Listado de Bandas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()