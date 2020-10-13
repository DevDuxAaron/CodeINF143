# Estudiante: Aaron Joel Limachi Quispe
# CI: 12732282

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fact_LU(arr, n):
    for j in range(2, n):
        arr[1][j] = arr[1][j] / arr[1][1]
    for j in range(2, n-1):
        for i in range(j, n):
            su = 0
            for k in range(1, j-1):
                su = su + arr[i][k] * arr[k][j]
            arr[i][j] = arr[i][j] - su
        for k in range(j + 1, n):
            su = 0
            for l in range(1, j-1):
                su = su + arr[j][l] * arr[l][k]
            arr[j][k] = (arr[j][k] - su) / arr[j][j]
    su = 0
    for k in range(1, n-1):
        su = su + arr[n - 1][k] * arr[k][n - 1]
    arr[n - 1][n - 1] = arr[n - 1][n - 1] - su
    return arr

def get_U(arr, n):
    u = np.array([[0.0 for i in range(n)] for i in range(n)])
    for i in range(n):
        for j in range(i):
            u[i][j] = 0
    for i in range(n):
        for j in range(i, n):
            u[i][j] = arr[i][j]
    return u

def get_L(arr, u, n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[i][j] - u[i][j]
    for i in range(n):
        arr[i][i] = 1
    return np.array(arr)

def get_D(arrL, b_res):
    return np.linalg.solve(arrL, b_res)

def get_X(arrU, d_res):
    return np.linalg.solve(arrU, d_res)

def show(foo, n, m):
    for i in range(n):
        for j in range(m):
            print(foo[i][j], end="\t")
        print()


if __name__ == '__main__':
    # A = np.array([
    #     [3, -0.1, -0.2],
    #     [0.1, 7, -0.3],
    #     [0.3, -0.2, 10]
    # ])
    # b = np.array([[7.85], [-19.3], [71.4]])
    A = np.array([
        [3.3330, 15920, -10.333],
        [2.2220, 16.710, 9.6120],
        [1.5611, 5.1791, 1.6852]
    ])
    b = np.array([[15913], [28.544], [8.4254]])

    AUX = A.copy()
    B_AUX = b.copy()
    nro = 3

    LU = fact_LU(A, nro)
    U = get_U(LU, nro)
    L = get_L(LU, U, nro)

    D = get_D(L, b)
    X = get_X(U, D)
    print(X)

    x = np.arange(0, 40, 0.5)
    y = np.arange(0, 40, 0.5)
    eje_x_1, eje_y_1 = np.meshgrid(x, y)
    eje_x_2, eje_y_2 = np.meshgrid(x, y)
    eje_x_3, eje_y_3 = np.meshgrid(x, y)

    eje_z_1 = float(B_AUX[0][0] / AUX[0][2]) - float(AUX[0][0] / AUX[0][2]) * eje_x_1 + float(AUX[0][1] / AUX[0][2]) * eje_y_1
    eje_z_2 = float(B_AUX[1][0] / AUX[1][2]) - float(AUX[1][0] / AUX[1][2]) * eje_x_2 + float(AUX[1][1] / AUX[1][2]) * eje_y_2
    eje_z_3 = float(B_AUX[2][0] / AUX[2][2]) - float(AUX[2][0] / AUX[2][2]) * eje_x_3 + float(AUX[2][1] / AUX[2][2]) * eje_y_3

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(eje_x_1, eje_y_1, eje_z_1, alpha=0.5, color='red')
    ax.plot_surface(eje_x_2, eje_y_2, eje_z_2, alpha=0.5, color='green')
    ax.plot_surface(eje_x_3, eje_y_3, eje_z_3, alpha=0.5, color='blue')
    plt.show()
