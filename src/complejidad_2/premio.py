casos = int(input())
for k in range(casos):
    n, a, b = map(int, input().split())
    if a == b:
        print(b * n, a * n, 1)
    else:
        print(min(a, b)*n, max(a, b)*n, n + 1)
