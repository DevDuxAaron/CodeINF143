n, e = map(int, input().split())
matrix = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))

matrix_auxB = matrix.copy()
for veces in range(e-1):
    matrix_auxC = [[0 for j in range(n)] for i in range(n)]
    for p in range(n):
        for q in range(n):
            for r in range(n):
                matrix_auxC[p][q] += matrix[p][r] * matrix_auxB[r][q]
    matrix_auxB = matrix_auxC.copy()
for k in matrix_auxC:
    for h in range(n-1):
        print(k[h],end=" ")
    print(k[-1])
