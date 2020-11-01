cases = int(input())
for _ in range(cases):
    nivel, q = map(int, input().split())
    nivel -= 1
    x = 1
    for i in range(nivel):
        if q % 2 == 0:
            x = (x * 2) + 1
            q /= 2
        else:
            x *= 2
            q = (q + 1)/2
    print(x)
