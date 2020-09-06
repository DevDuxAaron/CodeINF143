

def verify(x1, y1, x2, y2, x3, y3, x4, y4):
    col[x1 - 1] = y1 - 1
    col[x2 - 1] = y2 - 1
    col[x3 - 1] = y3 - 1
    col[x4 - 1] = y4 - 1



def search(y):
    global count
    if y == n:
        count += 1
    else:
        for x in range(n):
            if col[x] or diag1[x + y] or diag2[x - y + n - 1]:
                print(col, 'col')
                print(diag1, 'diag1')
                print(diag2, 'diag2')
                continue
            col[x] = y + 1
            diag1[x + y] = diag2[x - y + n - 1] = 1
            search(y + 1)
            col[x] = diag1[x + y] = diag2[x - y + n - 1] = 0


# x = int(input())
x = 1
for i in range(x):
    n = 4  # tamanio del tablero
    N = n * 2 - 1  # espacio para las diagonales
    col = [0] * n
    diag1 = [0] * N
    diag2 = [0] * N
    count = 0
    # x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    # verify(x1, y1, x2, y2, x3, y3, x4, y4)
    search(0)
    print(count)
