def fun(n, k):
    if k <= (n // 2):
        return (k // 2) + 1
    else:
        return ((n + 1 - k)//2) + 1


casos = int(input())
for i in range(casos):
    n, k = map(int, input().split())
    print(fun(n, k))
print(fun(6, 2))
print(fun(6, 5))
print(fun(10, 5))
print(fun(10, 4))
print(fun(10, 6))
print(fun(12, 6))
print(fun(12, 7))
