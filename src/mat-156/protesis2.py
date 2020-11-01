import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from math import tan
from math import pi

Lb = 182
H = 117
Lf = 28
Lm = 20
p = 29
placa = 3.54
lp1 = 13
lp2 = 6
Ldedo = 2.5
escala = 1.5
angulo = (pi/180)*25

y1 = Lb - H - Lm
y2 = Lf * 1.5
y3 = tan(angulo) * lp1
yp = (y1+y2)/2
r = p/(pi*2)
P1 = [(-r-placa, yp), (-r-placa, Lm), (-lp1, 12), (0, y3), (lp1, 0), (lp1 + lp2, Ldedo)]

Lba = 170
Ha = 90
Lfa = 10
Lma = 18
pa = 15
placaa = 3.54
lp1a = 10
lp2a = 3.5
Ldedoa = 1.5
escalaa = 1.5
anguloa = (pi/180)*15

y1a = Lba - Ha - Lma
y2a = Lfa * 1.5
y3a = tan(anguloa) * lp1a
ypa = (y1a+y2a)/2
ra = pa/(pi*2)
P2 = [(-ra-placaa, ypa), (-ra-placaa, Lma), (-lp1a, 12), (0, y3a), (lp1a, 0), (lp1a + lp2a, Ldedoa)]

xi, yi = zip(*P1)
xia, yia = zip(*P2)


points = np.array([xi, yi]).T
points1 = np.array([xia, yia]).T

distance = np.cumsum(np.sqrt(np.sum(np.diff(points, axis=0) ** 2, axis=1)))
distance = np.insert(distance, 0, 0) / distance[-1]

distance1 = np.cumsum(np.sqrt(np.sum(np.diff(points1, axis=0) ** 2, axis=1)))
distance1 = np.insert(distance1, 0, 0) / distance1[-1]

interpolations_methods = ['quadratic']
#interpolations_methodsL = ['linear']
alpha = np.linspace(0, 1, 75)

interpolated_points = {}
for method in interpolations_methods:
    interpolator = interp1d(distance, points, kind=method, axis=0)
    interpolated_points[method] = interpolator(alpha)
interpolated_points1 = {}
for method in interpolations_methods:
    interpolator = interp1d(distance1, points1, kind=method, axis=0)
    interpolated_points1[method] = interpolator(alpha)

# fig, axs = plt.subplots(1, 2, figsize=(7, 7))
plt.figure(figsize=(7, 7))
for method_name, curve in interpolated_points.items():
    plt.plot(*curve.T, '-', label=method_name, color='green')
for method_name, curve in interpolated_points1.items():
    plt.plot(*curve.T, '-', label=method_name, color='blue')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
