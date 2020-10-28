import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

def lagrange(xi, fi, n):
    x = sym.Symbol("x")
    polinomio = 0
    for i in range(n):
        num = 1
        dem = 1
        ter = 0
        for j in range(n):
            if i != j:
                num = num * (x - xi[j])
                dem = dem * (xi[i] - xi[j])
            ter = (num / dem) * fi[i]
        polinomio += ter
    polis = sym.expand(polinomio)
    px = sym.lambdify(x, polinomio)
    # Graficando
    EC = sym.lambdify(x, polis, 'numpy')
    t1 = np.linspace(0, 50, 50)
    plt.plot(t1, EC(t1))
    plt.show()
    return polis, px

def llenarLagrange():
    print("Lagrange")
    n = int(input("Introduzca el nro de puntos"))
    print("Introduzca los xi")
    x_i = list(map(float, input().split()))
    print("Introduzca los fi")
    f_i = list(map(float, input().split()))
    ec1, ec2 = lagrange(x_i, f_i, n)
    print("Ecuacion obtenida")
    print(ec1)

def splines(P):
    # Lista de tuplas con los puntos
    xi, yi = zip(*P)
    x = np.linspace(min(xi), max(xi), num=1001)
    y1d = np.interp(x, xi, yi)
    ysp = InterpolatedUnivariateSpline(xi, yi)(x)
    plt.plot(x, ysp)

    plt.show()

def llenarSplines():
    print("Spline")
    n = int(input("Ingrese el numero de puntos"))
    Pts = []
    for _ in range(n):
        print("Ingrese punto:", _+1)
        a, b = map(float, input().split())
        Pts.append((a, b))
    splines(Pts)


if __name__ == '__main__':
    llenarSplines()
    # llenarLagrange()


# 0 600 1500 2300 3000 6100 7900
# 100 98.8 95.1 92.2 90 81.2 75.6
# def func():
#     n = int(input("Ingrese el maximo exponente"))
#     f = 0
#     for i in range(n, -1, -1):
#         r = int(input("Ingrese el coeficiente de x^" + str(i)))
#
#
# def newton(fn, x, tol=0.00001, maxiter=100):
#     for i in range(maxiter):
#         xnew = x - fn[0](x) / fn[1](x)
#         if abs(xnew - x) < tol: break
#         x = xnew
#     return xnew, i
#
#
# def llenar_newton(y):
#     rx = float(input("Ingrese el x a Buscar: "))
#     xnew, i = newton(y, rx)
#     print("El resultado es %f en %d iteraciones." % (xnew, i))


# def splines(n, t, y):
#     h = [0] * n
#     b = [0] * n
#     for i in range(0, n - 1, 1):
#         h[i] = t[i + 1] - t[i]
#         b[i] = 6 * (y[i + 1] - y[i]) / h[i]
#     u = [0] * n
#     v = [0] * n
#     u[1] = 2 * (h[0] + h[1])
#     v[1] = b[1] - b[0]
#     for i in range(2, n, 1):
#         u[i] = 2 * (h[i] + h[i - 1]) - (h[i - 1] ** 2 / u[i - 1])
#         v[i] = b[i] - b[i - 1] - (h[i - 1] * v[i - 1] / u[i - 1])
#     z = [0] * (n + 1)
#     z[n] = 0
#     for i in range(n - 1, 0, -1):
#         z[i] = (v[i] - h[i] * z[i + 1]) / u[i]
#     z[0] = 0
#     return z


# def llenar_splines():
#     n = int(input("Introduzca el numero de puntos: "))
#     x = [0] * n
#     y = [0] * n
#     for i in range(0, n):
#         x[i], y[i] = map(float,
#                          input("Introduzca par de coordenadas (x" + str(i + 1) + "," + str(i + 1) + "y): ").split())
#     z = splines(n, x, y)
#     print(z)
