import numpy as np
import scipy.linalg
import re
import os


def seidel(A_seidel: np.ndarray, b: np.ndarray, eps=1e-5, maxiter=1000):
    D = np.diag(np.diag(A_seidel))
    L = np.tril(A_seidel)
    U = np.triu(A_seidel) - D
    inv = scipy.linalg.solve_triangular(L, np.eye(n), lower=True)  # Inversa optimizada
    invU = -(inv @ U)

    it = 0
    x0 = np.ones_like(b)
    x1 = x0 + eps * 1e1

    while np.linalg.norm(abs(x0 - x1)) > eps and it < maxiter:
        x0 = x1
        x1 = invU @ x0 + inv @ b
        it += 1
    return x1, it

def cool():
    print(" " * 15 + "Seidel")
    print("Estudiante: Aaron Joel LImachi Quispe")

def verify_n():
    auxiliar = input("Ingrese el tamanio de la matriz: ")
    foo = re.findall('[^0-9]', auxiliar)
    while len(foo) > 0 or len(auxiliar) == 0:
        auxiliar = input("Ingrese un valor numerico entero")
        foo = re.findall('[^0-9]', auxiliar)
    return int(auxiliar)

def verify(aux):
    foo = re.findall('[^0-9.-]', aux)
    while len(foo) > 0 or len(aux) == 0:
        aux = input("Ingrese un valor numerico")
        foo = re.findall('[^0-9.-]', aux)
    return float(aux)

def matrix(n):
    A = np.array([[0 for i in range(n)]]*n)
    # print(A)
    for i in range(n):
        for j in range(n):
            aux = input("Ingrese el para A[{}][{}]: ".format(i, j))
            A[i][j] = verify(aux)
    return A

def coeficient(n):
    b = np.array([0]*n)
    for i in range(n):
        aux = input("Ingrese el para b[{}]".format(i))
        b[i] = verify(aux)
    return b

def ask():
    x: str = input("Desea continuar:[S]i / [N]o")
    x = x.lower()
    foo = re.findall('[^sn]', x)
    while len(foo) > 0 or len(x) == 0:
        x = input("Ingrese [S]i / [N]o")
        foo = re.findall('[^sn]', x)
    return not(x == 'n')


if __name__ == '__main__':
    sw = True
    while sw:
        cool()
        n = verify_n()
        A = matrix(n)
        b = coeficient(n)
        clear = lambda: os.system('cls')  # para Windows
        clear()
        print("-"*15 + "A" + "-"*15)
        print(A)
        print("-" * 15 + "b" + "-" * 15)
        print(b)
        x1, iterations_1 = seidel(A, b, eps=1e-16)
        print('Residuo de: {} en {} iteraciones'.format(np.linalg.norm(A@x1 - b), iterations_1))
        print("-"*15 + "Vector solucion" + "-"*15)
        print(x1)
        print("-"*15 + "alfa" + "-"*15)
        print(np.linalg.norm(A@x1 - b))
        sw = ask()
        clear()



# rndm = np.random.RandomState(1234)
# Create a uniform system
# n = 5
# A = rndm.uniform(size=(n, n)) + np.diagflat([15]*n)
# b = rndm.uniform(size=n)
# A = np.array([
#     [10, -1, 2, 0],
#     [-1, 11, -1, 3],
#     [2, -1, 10, -1],
#     [0, 3, -1, 8]
# ])
# b = np.array([6, 25, -11, 15])
# print("-"*15 + "A" + "-"*15)
# print(A)
# print("-"*15 + "b" + "-"*15)
# print(b)

# dominant diagonal
# x1, iterations_1 = seidel(A, b, eps=1e-16)
# print('Residuo de: {} en {} iteraciones para una matriz diagonal dominante'.format(np.linalg.norm(A@x1 - b), iterations_1))
# print()
# print("-"*15 + "x1" + "-"*15)
# print(x1)
# print("-"*15 + "alfa" + "-"*15)
# print(np.linalg.norm(A@x1 - b))

# no dominant diagonal
# A2 = rndm.uniform(size=(n, n))
# x2, iterations_1 = siedel(A2, b, eps=1e-16)
# print(f'Residuo de: {np.linalg.norm(A2@x2 - b)} en {iterations_1} iteraciones para una matriz NO diagonal dominante')


# def fill_matrix(event):
#     n = int(ent_n.get()) if ent_n.get() != "" else 0
#     A = rndm.uniform(size=(n, n)) + np.diagflat([15] * n)
#     for i in range(n):
#         for j in range(n):
#             lbl_aux = tk.Label(
#                 text="Ingresa el valor para [{}][{}]: ".format(i, j),
#                 foreground=primary
#             )
#             ent_aux = tk.Entry(
#                 foreground=primary,
#                 width=5
#             )
#             # lbl_aux.place(x=((i*50)+150), y=((j*50)+150))
#             ent_aux.place(x=((i*50)+200), y=((j*50)+100))
#     btn_m = tk.Button(
#         text="Aceptar",
#         foreground="white",
#         background=extra,
#         width=25,
#     )
#     btn_m.place(x=((50*n)+210), y=((50*n)+210))

# if __name__ == "__main__":
#     primary = "#1752AA"
#     secondary = "#3CD90B"
#     extra = "#FF6C0D"
#
#     window = tk.Tk()
#     window.resizable(width=400, height=500)
#
#     lbl_title = tk.Label(
#         text="Metodo iterativo Seidel",
#         foreground=primary,
#         width=100,
#         height=1
#     )
#     lbl_n = tk.Label(
#         text="Ingresa el tamanio de la matriz: ",
#         foreground=primary,
#         width=25,
#         height=1
#     )
#     ent_n = tk.Entry(
#         width=25,
#     )
#     btn_n = tk.Button(
#         text="Aceptar",
#         foreground="white",
#         background=extra,
#         width=25,
#         height=1
#     )
#
#     lbl_title.pack()
#     lbl_n.pack()
#     ent_n.pack()
#     btn_n.pack()
#     btn_n.bind("<Button-1>", fill_matrix)
#     window.mainloop()
