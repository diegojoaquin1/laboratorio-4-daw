from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        return inverter.get(color, color)

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen (voltear izquierda-derecha) """
        espejo = []
        for fila in self.img:
            espejo.append(fila[::-1])
        return Picture(espejo)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen (voltear arriba-abajo) """
        espejo = self.img[::-1]
        return Picture(espejo)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negativo = []
        for fila in self.img:
            nueva_fila = ""
            for caracter in fila:
                nueva_fila += self._invColor(caracter)
            negativo.append(nueva_fila)
        return Picture(negativo)

    def join(self, p):
        """ Pone la figura p al lado derecho de la actual """
        unidas = []
        for i in range(len(self.img)):
            unidas.append(self.img[i] + p.img[i])
        return Picture(unidas)

    def up(self, p):
        """ Pone la figura p encima de la figura actual """
        # Simplemente sumamos las listas de strings
        nueva_img = p.img + self.img
        return Picture(nueva_img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual (superposición de caracteres) """
        combinada = []
        for i in range(len(self.img)):
            fila_nueva = ""
            for j in range(len(self.img[i])):
                # Si p tiene un color transparente (espacio), se queda el de self
                if p.img[i][j] == " ":
                    fila_nueva += self.img[i][j]
                else:
                    fila_nueva += p.img[i][j]
            combinada.append(fila_nueva)
        return Picture(combinada)

    def horizontalRepeat(self, n):
        """ Repite la figura n veces horizontalmente """
        repetida = []
        for fila in self.img:
            repetida.append(fila * n)
        return Picture(repetida)

    def verticalRepeat(self, n):
        """ Repite la figura n veces verticalmente """
        repetida = self.img * n
        return Picture(repetida)

    def rotate(self):
        """ Rota la figura 90 grados en sentido horario """
        rotada = []
        # Usamos el ancho de la primera fila para saber cuántas columnas hay
        for i in range(len(self.img[0])):
            nueva_fila = ""
            # Recorremos de abajo hacia arriba para la rotación horaria
            for j in range(len(self.img) - 1, -1, -1):
                nueva_fila += self.img[j][i]
            rotada.append(nueva_fila)
        return Picture(rotada)