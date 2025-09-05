class Participante:
    def __init__(self, nombre, institucion):
        super().__init__()
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        pass


class BandaEscolar(Participante):
    def __init__(self, nombre, institucion, categoria, puntajes):
        super().__init__(nombre, institucion)
        self._categoria = categoria
        self._puntajes = puntajes

    def set_categoria(self, categoria):
        if self._categoria == "primaria":
            self._categoria = categoria

        elif self._categoria == "básico":
            self._categoria = categoria

        elif self._categoria == "diversificado":
            self._categoria = categoria

        else:
            print("Categoria incorrecta")