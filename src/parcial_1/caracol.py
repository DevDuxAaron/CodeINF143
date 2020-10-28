t = int(input())
x = []
for i in range(t):
    line = list(map(int, input().split()))
    x.extend(line)
x.sort()
r = [[0 for i in range(t)] for j in range(t)]
for i in range(t):
    r[0][i] = x[i]

aux = t - 1
xi = 0
yi = t - 1
c = t
sent = -1
cont = 0
sw = 1
# cant lines
for i in range((t - 1) * 2):
    # long line
    for j in range(aux):
        if cont == 0:
            xi += sent * (-1)
        elif cont == 1:
            yi += sent
        elif cont == 2:
            xi += sent
        elif cont == 3:
            yi += sent * (-1)
        r[xi][yi] = x[c]
        c += 1
    cont = (cont + 1) % 4
    if sw == 2:
        aux -= 1
        sw = 0
    sw += 1

for _ in r:
    for __ in _:
        print(__, end=" ")
    print()
