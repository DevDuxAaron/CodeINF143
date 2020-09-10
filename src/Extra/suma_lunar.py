while True:
    try:
        x, y = input().split()
        res = ""
        for i in range(len(x)):
            res += str(max(int(x[i]), int(y[i])))
        print(res)
    except EOFError:
        break
