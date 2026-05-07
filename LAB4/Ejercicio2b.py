from interpreter import draw
from chessPictures import *


par_caballos1 = knight.join(knight.negative())
par_caballos2= knight.negative().join(knight)

par_caballos_invertidos = par_caballos2.verticalMirror().negative()
cuadrado = par_caballos_invertidos.up(par_caballos1)


draw(cuadrado)