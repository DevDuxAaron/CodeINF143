t = int(input())
aux = dict()
for _ in range(t):
    a, b = map(int, input().split())
    foo = a / b
    if foo in aux:
        aux[foo] += 1
    else:
        aux[foo] = 1
print(max(aux.values()))
