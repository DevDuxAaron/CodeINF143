import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

# Estudiante: Aaron Joel Limachi Quispe
# CI 12732282

# Arriba
P = [
     (2.0, 14.1),
     (3.0, 14.2),
     (6.0, 13.7),
     (7.0, 13.5),
     (7.5, 13.4),
     (8.0, 13.5),
     (11.0, 14.5),
     (12.0, 14.5),
     (15.0, 13.5),
     (15.8, 13.0),
     (17.0, 13.0),
     (21.0, 13.1),
     (22.0, 13.2)
]

# Ears
P_2 = [
     (2.0, 14.1),
     (3.5, 12.0),
     (5.0, 10.0),
     (7.8, 9.2),
     (11.5, 8.2),
     (16.0, 9.2),
     (19.0, 10.0),
     (22.0, 13.2)
]

# Details
P_3 = [
     (2.0, 14.1),
     (3.2, 13.7),
     (4.0, 13.5),
     (5.0, 13.0),
     (6.0, 12.5),
     (7.0, 12.0),
     (8.0, 9.0),
     (8.8, 8.8),
     (10.0, 8.9),
     (11.5, 8.3),
     (13.0, 8.7),
     (14.5, 8.9),
     (15.8, 9.2),
     (16.5, 10.5),
     (17.0, 11.2),
     (18.0, 11.7),
     (19.0, 12.0),
     (19.5, 12.1),
     (20.0, 12.2),
     (22.0, 13.2)
]

xi, yi = zip(*P)
xi_2, yi_2 = zip(*P_2)
xi_3, yi_3 = zip(*P_3)

print("Número de puntos: {}".format(len(xi) + len(xi_2) + len(xi_3)))

mini = min(min(xi), min(xi_2), min(xi_3))
maxi = max(max(xi), max(xi_2), max(xi_3))
x = np.linspace(mini, maxi, num=1001)
x_2 = np.linspace(mini, maxi, num=1001)
x_3 = np.linspace(mini, maxi, num=1001)

y1d = np.interp(x, xi, yi)
ysp = InterpolatedUnivariateSpline(xi, yi)(x)

y1d_2 = np.interp(x_2, xi_2, yi_2)
ysp_2 = InterpolatedUnivariateSpline(xi_2, yi_2)(x_2)

y1d_3 = np.interp(x_3, xi_3, yi_3)
ysp_3 = InterpolatedUnivariateSpline(xi_3, yi_3)(x_3)

# plt.plot(xi, yi, 'x', mew=2)
plt.plot(x, y1d)
plt.plot(x, ysp)

# plt.plot(xi_2, yi_2, 'g', mew=2)
plt.plot(x_2, y1d_2)
plt.plot(x_2, ysp_2)

# plt.plot(xi_3, yi_3, 'b', mew=2)
plt.plot(x_3, y1d_3)
plt.plot(x_3, ysp_3)

# Etiquetas
# leg = plt.legend(['Puntos', 'Lineal', 'Cúbico'])
# leg.get_frame().set_facecolor('#fafafa')

plt.show()
