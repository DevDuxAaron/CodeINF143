while True:
    try:
        n = int(input())
        x = 1
        a = 0
        while a < n:
            a = (x * (x + 1)) // 2
            x += 1
        x -= 2
        a = (x * (x + 1)) // 2
        print(n - a)
    except EOFError:
        break

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 1
# 1 2 3 4 5 6 7 8 9 1 0
# 1 2 3 4 5 6 7 8 9 1 0 1
