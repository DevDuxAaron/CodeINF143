def recursion(x, ni):
    print(x, ni)
    global c
    if len(x) == 4:
        c += 1 if x[0] ^ x[1] ^ x[2] ^ x[3] == 0 else 0
        return
    for i in range(ori[ni]):
        x.append(ori[i])
        recursion(x, ni+1)
        x.pop(-1)


c = 0
foo = int(input())
for _ in range(foo):
    ori = list(map(int, input().split()))
    recursion([], 0)
    print(c)
