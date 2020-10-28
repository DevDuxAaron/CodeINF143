t = int(input())
c = 0
aux = set([])
for _ in range(t):
    a, b, c, d = map(int, input().split())
    for A in range(1, a+1):
        for B in range(A, b+1):
            for C in range(B, c+1):
                for D in range(C, d+1):
                    if A ^ B ^ C ^ D == 0:
                        foo = [A, B, C, D]
                        foo.sort()
                        foo = ' '.join([str(item) for item in foo])
                        aux.add(foo)
    print(len(aux))
