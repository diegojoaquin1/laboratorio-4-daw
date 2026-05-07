from interpreter import draw
from chessPictures import *

cuadrado_negro = square.negative()
par_cuadrados = square.join(cuadrado_negro)
fila_cuadrados = par_cuadrados.horizontalRepeat(4)
doble_fila = fila_cuadrados.negative().up(fila_cuadrados)


draw(doble_fila.verticalRepeat(2))