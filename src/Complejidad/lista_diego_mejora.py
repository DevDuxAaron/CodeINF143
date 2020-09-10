while True:
    try:
        x, y, p = map(int, input().split())
        c = 0
        aux_x = x
        aux_y = y
        for i in range(p):
            if aux_x == aux_y:
                c = aux_y
                aux_x += x
                aux_y += y
            elif aux_x < aux_y:
                c = aux_x
                aux_x += x
            else:
                c = aux_y
                aux_y += y
        print(c)
    except EOFError:
        break
