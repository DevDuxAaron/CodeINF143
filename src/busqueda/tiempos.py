import sys
from time import time
import random

def bubble_sort1(A):
    c = 0
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                c += 1
    print(c)
    return


def insertion_sort2(A):
    c = 0
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j + 1] and j >= 0:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1
            c += 1
    print(c)


def insertion_sort3(A):
    c = 0
    for i in range(1, len(A)):
        curNum = A[i]
        k = 0
        for j in range(i - 1, -2, -1):
            k = j
            if A[j] > curNum:
                A[j + 1] = A[j]
                c += 1
            else:
                break
        A[k + 1] = curNum


def selection_sort(A):
    c = -1
    for i in range(0, len(A) - 1):
        minIndex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]
            c += 1

# def quick_sort2(A, low, hi):
#     if hi - low < threshold and low < hi:
#         quick_selection(A, low, hi)
#     elif low < hi:
#         p = partition(A, low, hi)
#         quick_sort2(A, low, p - 1)
#         quick_sort2(A, p + 1, hi)


def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)


def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle + 1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle + 1]
    R = A[middle + 1:last + 1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0

    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


if __name__ == '__main__':
    aux = 10 ** 6
    # A = [random.randint(0, aux) for i in range(aux)]
    # x = time()
    # bubble_sort1(A)
    # y = time()
    # print(y - x, "burbuja")

    # A = [random.randint(0,aux) for i in range(aux)]
    # x = time()
    # insertion_sort2(A)
    # y = time()
    # print(y - x, "insercion")

    # A = [random.randint(0,aux) for i in range(aux)]
    # x = time()
    # insertion_sort3(A)
    # y = time()
    # print(y - x, "insercion2")

    # A = [random.randint(0,aux) for i in range(aux)]
    # x = time()
    # selection_sort(A)
    # y = time()
    # print(y - x, "seleccion")

    A = [random.randint(0,aux) for i in range(aux)]
    x = time()
    merge_sort(A)
    y = time()
    print(y - x, "merge")

    A = [random.randint(0,aux) for i in range(aux)]
    x = time()
    A.sort()
    y = time()
    print(y - x, "De Python")

    print("-"*30)