from interpreter import draw
from chessPictures import *

cuadrado_negro = square.negative()
par_cuadrados = square.join(cuadrado_negro)
fila_cuadrados = par_cuadrados.horizontalRepeat(4)


draw(fila_cuadrados.negative())