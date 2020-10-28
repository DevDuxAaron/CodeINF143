t = int(input())
for _ in range(t):
    aux = set([])
    co = 0
    a, b, c, d = map(int, input().split())
    for A in range(1, min(a, b)+1):
        for B in range(A, min(c, d)+1):
            print(A, A, B, B)
            if A ^ A ^ B ^ B == 0:
                co += 1
    print(co)
