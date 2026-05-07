from interpreter import draw
from chessPictures import *

cuadrado_negro = square.negative()
par_cuadrados = square.join(cuadrado_negro)
fila_cuadrados = par_cuadrados.horizontalRepeat(4)
doble_fila = fila_cuadrados.negative().up(fila_cuadrados)
tablero = doble_fila.verticalRepeat(4)


fila_normal = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
fila_peones = pawn.horizontalRepeat(8)
fila_peones_negros  = pawn.horizontalRepeat(8).negative()
fila_normal_negros = fila_normal.negative()

piezas = fila_normal_negros.up(fila_peones_negros).up(doble_fila).up(doble_fila).up(fila_peones).up(fila_normal)

draw(tablero.under(piezas))