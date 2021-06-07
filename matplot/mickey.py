import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
def genSegmento(x = 0, y = 0, angulo = 1 , raio = 10):
  # Segmento de reta
   a= np.pi / 2 # Define o angulo
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
plt.figure(figsize=(10,10));

# ROSTO
genCirulo(0,0,10);
# ORELHAS 
genCirulo(10,10,4);
genCirulo(-10,10,4);

# OLHOS
genElipseV(-4 , 3, 3.5, 2);
genCirulo( -4 , 2, 1);
genElipseV(4 , 3, 3.5, 2);
genCirulo( 4 , 2, 1);


genParabola( 0, 0 ,4, -0.06);
genElipseH( 0 , -2, 2, 1);


genParabola( 0, -5 ,7, 0.06);
genParabola( 0, -7.25 ,4, 0.2);

plt.grid()
plt.show()