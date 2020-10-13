# Estudiante: Aaron Joel Limachi Quispe
# CI: 12732282
# Problema de Balanar

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

a, v, r = sp.symbols('a,v,r', real=True)
A, B, t, vo = sp.symbols('A,B,t,vo', positive=True)
# print(A, B, t, v, vo)

# Funcion original
a = A - B*v
print('Aceleracion')
print(a)
# Integrando para obtener la velocidad
i = 1 / (A - B*v)
i1 = sp.integrate(i, (v, vo, v))
# Obteninedo solucion de la ecuacion
v = sp.solve(i1 - t, v)
print('Velocidad')
print(v)

r = sp.integrate(v[0], (t, 0, t))
# print(r)

# Simplificando
r = r.collect((A - B*vo))
print('Desplazamiento')
print(r)

# Establecemos los valores para reemplazar en la ecuacion
val = {A: 10, B: 0.5, vo: 50}
# Creamos el espacio del grafico
t1 = np.linspace(0, 50, 50)

# Reemplazando valores Velocidad vs tiempo
v1 = v[0]
v2 = v1.subs(val)
V = sp.lambdify(t, v2, 'numpy')

# Reemplazando valores distancia vs tiempo
r = r.subs(val)
R = sp.lambdify(t, r, 'numpy')

# Reemplazando valores Aceleracion vs tiempo
Ac = A-B*v[0]
Ac = Ac.subs(val)
Ac = sp.lambdify(t, Ac, 'numpy')

val_4 = {A: 10, B: 0.5, vo: 50, t: 20}
v1_4 = v[0]
v2_4 = v1.subs(val_4)
print('La velocidad en t=20s es igual a: ', v2_4)

# Graficando
fig, axs = plt.subplots(3, figsize=(6, 6))
# fig.suptitle('Graficas para el movimiento de Balanar')
axs[0].plot(t1, Ac(t1))
axs[0].set_title('Aceleracion vs tiempo')
axs[0].set_xlabel('Tiempo(t)')
axs[0].set_ylabel('Aceleracion(a)')
axs[1].plot(V(t1), t1)
axs[1].set_title('Velocidad vs tiempo')
axs[1].set_xlabel('Tiempo(t)')
axs[1].set_ylabel('Velocidad(V)')
axs[2].plot(R(t1), t1)
axs[2].set_xlabel('Tiempo(t)')
axs[2].set_ylabel('Posicion(r)')
axs[2].set_title('Posicion vs tiempo')
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.95, wspace=0.1, hspace=0.6)
plt.show()

# Estudiante: Aaron Joel Limachi Quispe
# CI: 12732282