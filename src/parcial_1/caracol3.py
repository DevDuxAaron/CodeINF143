def caracol(nro, res):
    num = nro
    matrix = [[0 for x in range(num)] for y in range(num)]
    n = 0
    low = 0
    high = num - 1
    count = int((num + 1) / 2)
    for i in range(count):
        for j in range(low, high + 1):
            matrix[i][j] = res[n]
        for j in range(low + 1, high + 1):
            matrix[j][high] = res[n]
        for j in range(high - 1, low - 1, -1):
            matrix[high][j] = res[n]
        for j in range(high - 1, low, -1):
            matrix[j][low] = res[n]
        n += 1
        low += 1
        high -= 1
    for k in matrix:
        print(k)
        print(" ".join(k) +" ")


res = []
tam = int(input())
for i in range(tam):
    line = list(map(str, input().split()))
    res.extend(line)

res.sort()
caracol(tam, res)