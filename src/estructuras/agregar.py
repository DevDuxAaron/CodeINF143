while True:
    try:
        n = int(input())
        if n == 0:
            break
        nums = set(map(int, input().split()))
        ini = nums.pop()
        r = [0]*n
        r[0] = ini
        for i in range(1, n):
            x = nums.pop()
            r[i] += x + r[i-1]
        print(sum(r[1:]))
    except EOFError:
        break
