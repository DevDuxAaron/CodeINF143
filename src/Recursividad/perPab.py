def perPab(l, lo, count):
    aux = []
    for j in range(len(l)):
        aux.append(lo[l[j]-1])
    count += 1
    if aux == sorted(l):
        print(count)
    else:
        perPab(l, aux, count)


def pab(li, c):
    aux = []
    for i in range(n):
        aux.append(li[f[i]-1])
    c-=-1
    if aux == objective:
        print(c)
        return
    pab(aux, c)
    

t = int(input())
for i in range(t):
    n = int(input())
    f = list(map(int,input().split()))
    objective = [i for i in range(1, n+1)]
    pab(objective, 0)