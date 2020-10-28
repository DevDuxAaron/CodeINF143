t = int(input())
res = []
for i in range(t):
    line = input().split()
    res.extend(line)
res.sort()

derecha = True
izquierda = False
abajo = False
matrizc = [[0 for i in range(t)] for j in range(t)]
x = 0
y = -1
for k in range((t*t)):
    if izquierda:
        y -= 1
        if y == -1:
            y = 0
            x -= 1
            izquierda = False
        elif matrizc[x][y] != 0:
            y += 1
            x -= 1
            izquierda = False
    elif derecha:
        y += 1
        if y == t:
            y = t - 1
            x += 1
            derecha = False
            abajo = True
        elif matrizc[x][y] != 0:
            y -= 1
            x += 1
            derecha = False
            abajo = True
    elif abajo:
        x += 1
        if x == t:
            x = t - 1
            y -= 1
            abajo = False
            izquierda = True
        elif matrizc[x][y] != 0:
            y -= 1
            x -= 1
            abajo = False
            izquierda = True
    else:
        x -= 1
        if x == -1 or matrizc[x][y] != 0:
            x += 1
            y += 1
            derecha = True
    matrizc[x][y] = res[k]

for _ in matrizc:
    # print(_)
    foo = ""
    for __ in _:
        foo += str(__) + " "
    print(foo)
