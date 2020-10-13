import math

# a = math.round()

def show(a):
    for i in a:
        for j in range(len(i)):
            print(i[j], end="\t|\t")
        print()
    print()


matrix = [
    [1, -6, -2, 0, 0, 0],
    [0, 3, 4, 1, 0, 12],
    [0, 6, -2, 0, 1, 6]
]
aux = [[0 for i in range(6)] for j in range(3)]

while True:
    show(matrix)
    if min(matrix[0]) < 0:
        pivot_c = matrix[0].index(min(matrix[0]))
        a = matrix[1][len(matrix[1])-1] / matrix[1][pivot_c]
        b = matrix[2][len(matrix[2])-1] / matrix[2][pivot_c]
        if a < b:
            pivot = matrix[1][pivot_c]
            for i in range(6):
                aux[1][i] = matrix[1][i]/pivot
            for i in range(6):
                aux[0][i] = matrix[0][i] - (matrix[0][pivot_c] * aux[1][i])
            for i in range(6):
                aux[2][i] = matrix[2][i] - (matrix[2][pivot_c] * aux[1][i])
        else:
            pivot = matrix[2][pivot_c]
            for i in range(6):
                aux[2][i] = matrix[2][i] / pivot
            # file 1
            for i in range(6):
                o = matrix[0][i]
                p = matrix[0][pivot_c]
                e = aux[2][i]
                aux[0][i] = matrix[0][i] - (matrix[0][pivot_c] * aux[2][i])
            for i in range(6):
                aux[1][i] = matrix[1][i] - (matrix[1][pivot_c] * aux[2][i])
        matrix = aux.copy()
        aux = [[0 for i in range(6)] for j in range(3)]
    else:
        break
