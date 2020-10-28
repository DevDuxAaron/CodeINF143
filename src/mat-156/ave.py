import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

# Estudiante: Aaron Joel Limachi Quispe
# CI 12732282

P = [
     (0.9, 1.3),
     (1.3, 1.5),
     (1.9, 1.85),
     (2.1, 2.1),
     (2.6, 2.6),
     (3.0, 2.7),
     (3.9, 2.4),
     (4.4, 2.15),
     (4.7, 2.05),
     (5.0, 2.1),
     (6.0, 2.25),
     (7.0, 2.3),
     (8.0, 2.25),
     (9.2, 1.95),
     (10.5, 1.4),
     (11.3, 0.9),
     (11.6, 0.7),
     (12.0, 0.6),
     (12.6, 0.5),
     (13.0, 0.4),
     (13.3, 0.25)
]

xi, yi = zip(*P)

print("Número de puntos: {}".format(len(xi)))

mini = min(xi)
maxi = max(xi)
x = np.linspace(mini, maxi, num=1001)

y1d = np.interp(x, xi, yi)
ysp = InterpolatedUnivariateSpline(xi, yi)(x)

# plt.plot(xi, yi, 'x', mew=2)
# plt.plot(x, y1d)
plt.plot(x, ysp)

plt.show()
