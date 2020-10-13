while True:
    try:
        n = int(input())
        a = input().split()
        b = input().split()
        a.sort()
        for i in a:
            if i in b:
                b.pop(b.index(i))
        print(len(b))
    except EOFError:
        break
