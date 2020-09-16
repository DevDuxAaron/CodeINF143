n, v = map(int, input().split())
x = input().split()
x = {i: x[i] for i in range(n)}
r = {i: 0 for i in range(n)}
for i in range(n):
    r[(i + v) % n] = x[i]
# print(x.values())
re = ""
for i in r.values():
    re += i + " "
print(re)


