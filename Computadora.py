from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora(Raton, Teclado, Monitor):
    contador_computadoras = 0

    def __init__(self, nombre, raton, teclado, monitor):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._raton = raton
        self._teclado = teclado
        self._monitor = monitor

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def raton(self):
        return self._raton
    @raton.setter
    def raton(self, raton):
        self._raton = raton

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def nombre(self, monitor):
        self._monitor = monitor

    def __str__(self):
        return f"Id: {self._id_computadora}{self._nombre}: \n Monitor: {self._monitor} \n Teclado: {self._teclado} \n Raton: {self._raton} \n"

raton1 = Raton("USB", "HP")
raton2 = Raton("Bluetooth", "LG")
teclado1 = Teclado("Bluetooth", "Sony")
teclado2 = Teclado("USB", "Logitech")
monitor1 = Monitor("LG", "25 Pulgadas")
monitor2 = Monitor("Samsung", "14 Pulgadas")

computadora1 = Computadora("Razor One", raton1, teclado1, monitor1)
computadora2 = Computadora("PC Bit", raton2, teclado2, monitor2)