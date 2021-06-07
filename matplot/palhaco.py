# palhaço
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
def genSegmento(x = 0, y = 0, angulo = 2 , raio = 10):
  # Segmento de reta
  a = np.pi / angulo # Define o angulo
  # Determina o alcance do segmento de reta
  rx = x + np.linspace(0, raio * np.cos(a), 100);
  ry = y + np.linspace(0, raio * np.sin(a), 100);
  plt.plot(rx, ry);

def genCirulo(x = 0, y = 0, raio = 10):
  trajeto = np.linspace(0, 2 * np.pi, 100)
  # Circulo
  # xc, yc = 0, 0  # define o centro
  cx = raio * np.cos(trajeto) + x;
  cy = raio * np.sin(trajeto) + y;
  plt.plot(cx, cy);
# Gera baseado em uma equação parametrica
def genElipseH(x = 0, y = 0, a = 5, b = 3):
  trajeto = np.linspace(0, 2 * np.pi, 100);
  # HORIZONTAL ELIPSE
  a;  # radius x Comprimento Horizontal BASE
  b;  # radius y COmprimento Vertical   ALTURA
  cx = a * np.cos(trajeto) + x;
  cy = b * np.sin(trajeto) + y;
  plt.plot(cx, cy);
def genElipseV(x = 0, y = 0, a = 5, b = 2):
  trajeto = np.linspace(0, 2 * np.pi, 100);
  # VERTICAL  ELIPSE
  a;  # radius x Comprimento Horizontal ALTURA
  b; # radius y COmprimento Vertical   BASE
  cx = b * np.cos(trajeto) + x;
  cy = a * np.sin(trajeto) + y;
  plt.plot(cx, cy);
def genParabola(x = 0, y = 0, raio = 3, amplitude = 1 ):
  trajeto = np.linspace( raio * (-1), raio, 100);
  # Cuidado com Angulos Hiberbolicos kkkk
  px = trajeto;
  py = amplitude * ( trajeto - x)**2 + y;
  plt.plot( px, py );
def genHiberbole(x = 0, y = 0, raio = 5, amplitude = 5, distancia_focais = 1.5):
  trajeto = np.linspace( -raio, raio, 100);
  a = amplitude
  b = distancia_focais #Define a distancia entre os focais
  x_dir = a * np.cosh(trajeto  ) + x
  x_esq = -a * np.cosh(trajeto ) + x
  y_trajeto = b * np.sinh(trajeto) + y

  plt.plot(x_dir   , y_trajeto );
  plt.plot(x_esq , y_trajeto );
plt.figure(figsize=(10,10));

# FACE
genCirulo(0,0,10);

# ROSTO
#  OLHOS
genHiberbole(0, 3.5, 2, 1.5, 0.5);
#  NARIS
genCirulo(0,0,2);
#  BOCA
genParabola( 0, -5 ,7.2, 0.08);
genParabola( 0, -5.25 ,1.7, -0.5);
genParabola( 0, -7.1 ,7.2, 0.12);


# CHAPEU
# Usando segmento de reta
# 10 cirdulo  
genSegmento(   0,   10,    5, 10 - 1.5);

genSegmento( 7.5,  6.5,  1.9, 10 - 1.5);

# Faltando hiberbole nos olhos

plt.grid()
plt.show()