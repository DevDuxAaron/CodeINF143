n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    p = b // a
    aux = p + b
    while True:
        s = aux // a
        if s == p:
            break
        p = s
        aux = p + b
    print(aux)

# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
