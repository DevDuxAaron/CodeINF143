while True:
    try:
        a, b = map(int, input().split())
        x = a | b
        y = a & b
        z = a & (~b)
        print(x,y,z)
    except EOFError:
        break
