# import numpy as np
# import matplotlib.pyplot as plt
# import sympy as sp
# a, v, r = sp.symbols('a,v,r', real=True)
# m, t, b, g, vo = sp.symbols('m,t,v,g,vo', positive=True)
# a = g - (b*v/m)
# i = 1 / (g - (b*v/m))
# i1 = sp.integrate(i, (v, vo, v))
# v = sp.solve(i1 - t, v)
# r = sp.integrate(v[0], (t, 0, t))
# r = r.expand(power_exp=True)
# r = r.collect(m*g/b)
# r = r.collect(m*vo/b)
# val = {b: 0.4, m: 1, vo: 50, g: 9.81}
# t1 = np.linspace(0, 20, 1000)
# fig = plt.figure('solution')
# fig.set_title("Titulo")
# plt.subplot(3, 1, 1)
# v1 = v[0]
# v2 = v1.subs(val)
# V = sp.lambdify(t, v2, 'numpy')
# plt.plot(t1, V(t1))
# plt.axhline(0, color='r')
# plt.axvline(0, color='r')
# plt.subplot(3, 1, 2)
# r = r.subs(val)
# R = sp.lambdify(t, r, 'numpy')
# plt.plot(t1, R(t1))
# plt.axhline(0, color='r')
# plt.axvline(0, color='r')
# plt.subplot(3, 1, 3)
#
# A = g-b*v[0]/m
# A = A.subs(val)
# A = sp.lambdify(t, A, 'numpy')
# plt.plot(t1,A(t1))
# plt.axhline(0, color='r')
# plt.axvline(0, color='r')
# plt.show()
#
# xx = sp.symbols('x')
# aa = sp.Integral(sp.cos(xx)*sp.exp(xx), xx)
# sp.Eq(aa, aa.doit())


# plt.figure('solution')
# plt.subplot(3, 1, 1)
# plt.plot(t1, V(t1))
# plt.axhline(0, color='r')
# plt.axvline(0, color='r')
#
# plt.subplot(3, 1, 2)
# plt.plot(t1, R(t1))
# plt.axhline(0, color='r')
# plt.axvline(0, color='r')
#
# plt.subplot(3, 1, 3)
# plt.plot(t1,Ac(t1))
# plt.axhline(0, color='r')
# plt.axvline(0, color='r')
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
