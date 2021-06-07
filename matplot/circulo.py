# Circulo basico
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(-np.pi, np.pi, 100)
r = 10
# Circulo
xc, yc = 0, 0  # define o centro
cx = r * np.cos(t) + xc
cy = r * np.sin(t) + xc

# Segmento de reta
a = np.pi / 2 # Define o angulo
rx = xc + np.linspace(0, r * np.cos(a), 100)
ry = yc + np.linspace(0, r * np.sin(a), 100)


plt.figure(figsize=(8,8))
plt.plot(cx, cy)
plt.plot(rx, ry)
valores_x = list(range(xc - r, xc + r +1));
valores_y = list(range(yc - r, yc + r +1));
plt.xticks(valores_x);
plt.yticks(valores_y);
plt.grid()
plt.show()