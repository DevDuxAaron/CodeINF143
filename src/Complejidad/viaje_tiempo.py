import sys

enter = sys.stdin
n = int(enter.readline())
for k in range(n):
    conteo = [0]*10
    a = int(enter.readline())
    x = input().split()
    for i in x:
        conteo[int(max(i))] += 1
    print(conteo.index(max(conteo)))
