from interpreter import draw
from chessPictures import *

# Colores
s = square          # casilla clara
n = square.negative()  # casilla oscura
e = " "             # transparente (vacío)

def empty_piece(base_square):
    """Pieza vacía: solo la casilla de fondo"""
    return base_square

# Construir tablero base (a8 arriba-izquierda = oscura)
par_OS = n.join(s)   # oscura-clara
par_SO = s.join(n)   # clara-oscura

fila_OS = par_OS.horizontalRepeat(4)  # empieza oscura
fila_SO = par_SO.horizontalRepeat(4)  # empieza clara

# Par de filas alternadas
doble_OS = fila_OS.up(fila_SO)   # fila8,fila7 pattern
doble_SO = fila_SO.up(fila_OS)

tablero = doble_SO.verticalRepeat(2).up(doble_OS.verticalRepeat(2))

# Helpers: pieza sobre casilla correcta
def pc(pieza, casilla):
    return casilla.under(pieza)

B = bishop
Q = queen
K = king
R = rock
Kn = knight
P = pawn

# Negros
bR = n.under(R.negative())
bB = s.under(B.negative())
bBn= n.under(B.negative())
bQ = n.under(Q.negative())
bK = s.under(K.negative())
bKn= s.under(Kn.negative())
bKnn=n.under(Kn.negative())
bP = lambda sq: sq.under(P.negative())

# Blancos
wR = s.under(R)
wB = s.under(B)
wQ = s.under(Q)
wK = s.under(K)
wKn= s.under(Kn)
wP = lambda sq: sq.under(P)

# Fila 8: a8=R_n, b8=vacio_s, c8=B_s, d8=Q_n, e8=K_s, f8=B_n, g8=Kn_s(?), h8=R_n
# Colores de casillas fila 8 (fila par desde arriba): a8=dark,b8=light,c8=dark... 
# a8 oscura, b8 clara, c8 oscura, d8 clara, e8 oscura... wait
# a8=dark, b8=light, c8=dark, d8=light, e8=dark, f8=light, g8=dark, h8=light
f8 = (n.under(R.negative())).join(s).join(n.under(B.negative())).join(s.under(Q.negative())).join(n.under(K.negative())).join(s.under(B.negative())).join(n.under(Kn.negative())).join(s.under(R.negative()))

# Fila 7: a7=p, b7=vacio, c7=p, d7=p, e7=vacio, f7=p, g7=p, h7=p
# a7=light, b7=dark, c7=light, d7=dark, e7=light, f7=dark, g7=light, h7=dark
f7 = s.under(P.negative()).join(n).join(s.under(P.negative())).join(n.under(P.negative())).join(s).join(n.under(P.negative())).join(s.under(P.negative())).join(n.under(P.negative()))

# Fila 6: a6=vacio, b6=vacio, c6=Kn_negro, resto vacio
# a6=dark,b6=light,c6=dark,d6=light,e6=dark,f6=light,g6=dark,h6=light
f6 = n.join(s).join(n.under(Kn.negative())).join(s).join(n).join(s).join(n).join(s)

# Fila 5: e5=peon negro
# a5=light,b5=dark,c5=light,d5=dark,e5=light,f5=dark,g5=light,h5=dark
f5 = s.join(n).join(s).join(n).join(s.under(P.negative())).join(n).join(s).join(n)

# Fila 4: c4=bishop blanco, d4=peon blanco
# a4=dark,b4=light,c4=dark,d4=light,e4=dark,f4=light,g4=dark,h4=light
f4 = n.join(s).join(n.under(B)).join(s.under(P)).join(n).join(s).join(n).join(s)

# Fila 3: f3=knight blanco
# a3=light,b3=dark,c3=light,d3=dark,e3=light,f3=dark,g3=light,h3=dark
f3 = s.join(n).join(s).join(n).join(s).join(n.under(Kn)).join(s).join(n)

# Fila 2: a2,b2,d2,f2,g2 = peones blancos
# a2=dark,b2=light,c2=dark,d2=light,e2=dark,f2=light,g2=dark,h2=light
f2 = n.under(P).join(s.under(P)).join(n).join(s.under(P)).join(n).join(s.under(P)).join(n.under(P)).join(s)

# Fila 1: a1=R, b1=Kn, c1=B, d1=Q, e1=K, f1=vacio, g1=vacio, h1=R
# a1=light,b1=dark,c1=light,d1=dark,e1=light,f1=dark,g1=light,h1=dark
f1 = s.under(R).join(n.under(Kn)).join(s.under(B)).join(n.under(Q)).join(s.under(K)).join(n).join(s).join(n.under(R))

piezas = f8.up(f7).up(f6).up(f5).up(f4).up(f3).up(f2).up(f1)

draw(piezas)