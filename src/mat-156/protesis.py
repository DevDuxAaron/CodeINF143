import numpy as np
from math import tan
from math import pi
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.interpolate import UnivariateSpline


def getKey(item):
    return item[0]


# Caso 1
Lb = 182
H = 117
Lf = 28
Lm = 20
p = 29
placa = 3.54
Lp1 = 13
Lp2 = 6
Ldedo = 2.5
escala = 1.5
angulo = (pi/180)*25

# Caso 2
# Lb = 170
# H = 90
# Lf = 10
# Lm = 18
# p = 15
# placa = 3.54
# Lp1 = 10
# Lp2 = 3.5
# Ldedo = 1.5
# escala = 1.5
# angulo = (pi/180)*15

# Caso abierto
# Lb = float(input())
# H = float(input())
# Lf = float(input())
# Lm = float(input())
# p = float(input())
# placa = float(input())
# Lp1 = float(input())
# Lp2 = float(input())
# Ldedo = float(input())
# escala = float(input())
# angulo = float(input())

y1 = Lb - H - Lm
y2 = Lf * 1.5
y3 = tan(angulo) * Lp1
yp = (y1 + y2)/2
r = p/(pi * 2)

aux = abs(-r-placa)

P1 = [
    (-Lp1, 12.0),
    (-r-placa, Lm),
    (-r-placa + 0.5, yp),
]
P2 = [
    (-Lp1, 12.0),
    (0, y3),
    (Lp1, 0.0),
    (Lp1 + Lp2, Ldedo)
]

xi, yi = zip(*P1)
xi_2, yi_2 = zip(*P2)
print(xi, xi_2)
print(yi, yi_2)

x = np.linspace(min(xi), max(xi), num=1001)
x_2 = np.linspace(min(xi_2), max(xi_2), num=1001)

y1d = np.interp(x, xi, yi)
y1d2 = np.interp(x_2, xi_2, yi_2)

# ysp = InterpolatedUnivariateSpline(xi, yi, k=3)(x)
ysp_2 = InterpolatedUnivariateSpline(xi_2, yi_2, k=3)(x_2)

# Puntos
plt.plot(xi, yi, 'x', mew=2)
plt.plot(xi_2, yi_2, 'x', mew=2)

# Lineas
plt.plot(x, y1d)
# plt.plot(x_2, y1d2)

# Curva
# plt.plot(x, ysp)
plt.plot(x_2, ysp_2)

plt.show()
