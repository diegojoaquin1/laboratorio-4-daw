from interpreter import draw
from chessPictures import *

par_caballos1 = knight.join(knight.negative())
par_caballos2 = knight.negative().join(knight)
cuadrado = par_caballos2.up(par_caballos1)


draw(cuadrado)

