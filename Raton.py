from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(tipo_entrada, marca)
    def __str__(self):
        return f"Id: {self._id_raton}, Marca: {self.marca}, Tipo_Entrada: {self.tipo_entrada}"