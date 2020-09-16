casos = int(input())
for k in range(casos):
    n = int(input())
    posi = [0] * (n + 1)
    for i in range(1, n+1):
        for j in range(0, n, i):
            if posi[j] == 1:
                posi[j] = 0
            else:
                posi[j] = 1
        # print(posi)
    print(posi[1:].count(1), posi[1:].count(0))
