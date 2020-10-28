n = int(input())
x = list(map(int, input().split()))
for i in range(n-1):
    if x[i] % 2 == 1 and x[i] + 2 == x[i+1]:
        print(x[i], x[i+1])

