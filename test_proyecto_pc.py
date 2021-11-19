from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado

raton1 = Raton("USB", "HP")
raton2 = Raton("Bluetooth", "LG")
teclado1 = Teclado("Bluetooth", "Sony")
teclado2 = Teclado("USB", "Logitech")
monitor1 = Monitor("LG", "25 Pulgadas")
monitor2 = Monitor("Samsung", "14 Pulgadas")
monitor3 = Monitor("Sentey", "28 Pulgadas")

computadora1 = Computadora("Lenovo", raton1, teclado1, monitor1)
computadora2 = Computadora("Acer", raton2, teclado2, monitor2)
computadora3 = Computadora("Gamer", raton2, teclado1, monitor3)

computadoras1 = [computadora1, computadora3]
computadoras2 = [computadora2, computadora1]

orden1 = Orden(computadoras1)
orden2 = Orden(computadoras2)
print(orden1)
print(orden2)

orden1.agregar_computadora(computadora2)
print(orden1)