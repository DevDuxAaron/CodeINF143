casos = int(input())
for i in range(casos):
    n, obj = map(int, input().split())
    l1 = list(map(int, input().split()))
    lis = [(i, "n") for i in l1]
    r = lis[obj]
    lis[obj] = (r[0], 'z')
    r = lis[obj]
    mayor = max(lis)
    c = 0
    while max(lis) != r:
        while mayor in lis:
            elim = lis.pop(0)
            if elim != mayor:
                lis.append(elim)
            else:
                c += 1
                break
        mayor = max(lis)
    for k in lis:
        if k[0] == r[0]:
            c += 1
        if k == r:
            break
    print(c)
