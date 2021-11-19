from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(tipo_entrada, marca)
    def __str__(self):
        return f"Id: {self._id_teclado}, Marca: {self.marca}, Tipo_Entrada: {self.tipo_entrada}"