para_x = (6, 2, 4, 8, 6)
para_y = (1, 3, 9, 7, 1)
while True:
    try:
        x, y = map(int, input().split())
        x = para_x[x % 4]
        y = para_y[y % 4]
        print((x + y) % 10)
    except EOFError:
        break