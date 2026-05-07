# ♟️ Tablero de Ajedrez con Python - Laboratorio 04 (DAW)

Este proyecto implementa una aplicación en Python que aplica el principio de **separación de intereses**, modelando figuras de ajedrez como listas de strings (modelo) y visualizándolas con `pygame` a través del método `draw` (vista). El laboratorio demuestra el uso de programación orientada a objetos, manipulación de estructuras de datos y entornos virtuales en Python.

---

## 🚀 Características Principales

- **Separación de intereses**: El modelo (`Picture`) opera sobre arreglos de strings de forma completamente independiente de la capa gráfica.
- **Clase Picture**: Implementación de métodos como espejos, negativos, combinaciones y repeticiones de figuras.
- **Visualización con pygame**: Renderizado gráfico a través del método `draw` importado desde `interpreter`.
- **Entorno virtual**: Gestión de dependencias aislada mediante `venv` y `requirements.txt`.
- **7+ Ejercicios progresivos**: Desde figuras simples hasta el tablero completo con aperturas de ajedrez.

---

## 📂 Estructura del Proyecto

```
ajedrez/
├── chessPictures.py       # Biblioteca con los objetos de piezas disponibles
├── pieces.py              # Representación interna de piezas (arreglos de strings)
├── picture.py             # Clase Picture con los métodos implementados
├── colors.py              # Valores negativos de cada carácter de color
├── interpreter.py         # Método draw para visualización con pygame
├── main.py                # Punto de entrada / pruebas generales
├── Ejercicio2a.py         # Caballos: espejo vertical y horizontal
├── Ejercicio2b.py         # Caballos: espejo horizontal primero
├── Ejercicio2c.py         # Reinas en fila horizontal
├── Ejercicio2d.py         # Tablero de grises (negativo horizontal)
├── Ejercicio2e.py         # Patrón de grises con desplazamiento
├── Ejercicio2f.py         # Tablero vacío 8×8
├── Ejercicio2g.py         # Tablero inicial completo
├── requirements.txt       # Dependencias del proyecto (pygame)
└── img/                   # Capturas de los resultados visuales
```

---

## ⚙️ Métodos Implementados en `Picture`

La clase `Picture` tiene un único atributo `img` (lista de strings). Los métodos implementados son:

| Método | Descripción |
|---|---|
| `verticalMirror()` | Devuelve el espejo vertical de la imagen |
| `horizontalMirror()` | Devuelve el espejo horizontal de la imagen |
| `negative()` | Devuelve el negativo de la imagen (invierte colores) |
| `join(picture)` | Coloca `picture` al lado derecho de la figura actual |
| `up(picture)` | Coloca `picture` encima de la figura actual |
| `under(picture)` | Coloca `picture` debajo de la figura actual |
| `horizontalRepeat(n)` | Repite la figura `n` veces horizontalmente |
| `verticalRepeat(n)` | Repite la figura `n` veces verticalmente |

---

## 🐍 PASOS A SEGUIR

### 1. Creamos el entorno virtual

### 2. Activamos el entorno virtual

## 🧩 Ejercicios

### Ejercicio (a) – Caballos: espejo vertical y horizontal
Se construye una figura con cuatro caballos usando `join` y `horizontalMirror` / `verticalMirror`.
<img width="237" height="242" alt="WhatsApp Image 2026-05-07 at 1 37 36 PM" src="https://github.com/user-attachments/assets/eb4189e1-8827-4181-94da-c9d06e2d5b65" />

---

### Ejercicio (b) – Caballos: espejo horizontal primero
Variante del ejercicio anterior aplicando primero el espejo horizontal.
<img width="203" height="173" alt="WhatsApp Image 2026-05-07 at 1 38 50 PM" src="https://github.com/user-attachments/assets/a315f458-2835-4148-99bb-a8e638baac97" />


---

### Ejercicio (c) – Reinas en fila horizontal
Se repite la reina horizontalmente usando `horizontalRepeat`.
<img width="311" height="137" alt="WhatsApp Image 2026-05-07 at 1 39 38 PM" src="https://github.com/user-attachments/assets/cc7f28e9-5680-42b5-b866-6108d499c769" />


---

### Ejercicio (d) – Tablero de grises (negativo horizontal)
Se genera un patrón de casillas grises usando `negative` y `join` / `horizontalRepeat`.
<img width="627" height="140" alt="WhatsApp Image 2026-05-07 at 1 40 42 PM" src="https://github.com/user-attachments/assets/6963a820-7e77-4a90-aef3-167f5644aaa9" />


---

### Ejercicio (e) – Patrón de grises con desplazamiento
Variante del ejercicio (d) con el patrón desplazado una columna.
<img width="620" height="173" alt="WhatsApp Image 2026-05-07 at 1 44 19 PM" src="https://github.com/user-attachments/assets/a6bced71-598f-4c59-b0ad-cc6d0a23f360" />


---

### Ejercicio (f) – Tablero vacío 8×8
Se construye un tablero de ajedrez vacío usando `horizontalRepeat` y `verticalRepeat`.
<img width="642" height="353" alt="WhatsApp Image 2026-05-07 at 1 48 50 PM" src="https://github.com/user-attachments/assets/bcc29777-c885-466c-8131-089d4706912a" />


---

### Ejercicio (g) – Tablero inicial de ajedrez
Se arma el tablero completo con todas las piezas en su posición inicial usando `join`, `under` y `up`.
<img width="627" height="635" alt="WhatsApp Image 2026-05-07 at 2 51 23 PM" src="https://github.com/user-attachments/assets/aba45364-fc4a-4853-978f-0d72335f3dfa" />


---

### Ejercicio (h) – Apertura Italiana
Se muestra el tablero tras los movimientos `1.e4 e5 2.Cf3 Cc6 3.Ac4`. Las blancas desarrollan su alfil para presionar el peón de f7 y controlar el centro.
<img width="593" height="631" alt="WhatsApp Image 2026-05-07 at 3 04 37 PM" src="https://github.com/user-attachments/assets/2de232c8-2cc5-400f-a9fc-fc5df593c889" />

## 📺 Demostración en Video

Para una explicación detallada del funcionamiento, la implementación de los métodos y la visualización de los ejercicios, puedes ver el siguiente video:

URL: https://youtu.be/KC7rXuYIXfM
