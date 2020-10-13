import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import random


# ---------------------------------------
# Insertion Sort
# ---------------------------------------
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
    c = 0
    for i in range(1, len(A)):
        for j in range(i - 1, -1, -1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                c = c + 1
                if c % 50 == 0 or c == 1:
                    line1.set_ydata(A)
                    fig.canvas.draw()
            else:
                break
    line1.set_ydata(A)
    fig.canvas.draw()


# not optimized, equiv to break version, but uses while loop
def insertion_sort2(A):
    c = 0
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j + 1] and j >= 0:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1
            c = c + 1
            if c % 50 == 0 or c == 1:
                line1.set_ydata(A)
                fig.canvas.draw()
    line1.set_ydata(A)
    fig.canvas.draw()


# optimized - shifts instead of swapping
def insertion_sort3(A):
    c = 0
    for i in range(1, len(A)):
        curNum = A[i]
        k = 0
        for j in range(i - 1, -2, -1):
            k = j
            if A[j] > curNum:
                A[j + 1] = A[j]
                c = c + 1
                if c % 50 == 0 or c == 1:
                    line1.set_ydata(A)
                    fig.canvas.draw()
            else:
                break
        A[k + 1] = curNum
    line1.set_ydata(A)
    fig.canvas.draw()


tamano = 200
tamano = int(input('Tamaño (' + str(tamano) + ')'))
if tamano == 0:
    tamano = 200
tipo = int(input('0. Aleatorio 1. Desendente 2. Acendente'))
x = [_ for _ in range(tamano)]
y = [random.randint(0, 50) for _ in range(tamano)]
if tipo == 1:
    y.sort(reverse=True)
elif tipo == 2:
    y.sort()
fun = {1: insertion_sort1, 2: insertion_sort2, 3: insertion_sort3}
sel = int(input('1:insertion_sort1,2:insertion_sort2,3:insertion_sort3: '))
f = fun[sel]
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, '.')
f(y)
time.sleep(5)
