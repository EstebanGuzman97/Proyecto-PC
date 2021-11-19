from Computadora import Computadora
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Orden(Computadora):
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f"Orden: {self._id_orden} \n Computadoras: {computadoras_str}"