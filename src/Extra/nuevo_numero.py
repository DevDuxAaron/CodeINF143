x = int(input())
for _ in range(x):
    num, times = input().split()
    # num = num[-1::-1]
    ind = ""
    for i in range(len(num)-(int(times)-1)):
        res = 0
        for j in range(i, i+int(times)):
            res += int(num[j])
        while len(str(res)) > 1:
            res = (res // 10) + (res % 10)
        ind += str(res)
    print(ind)
