try:
    x = int(input())
    for i in range(x):
        blank = input()
        n, k = map(int, input().split())
        for i in range(2**n):
            if bin(i).count("1") == k:
                if len(bin(i))-2 != n:
                    foo = "0"*((n+2) - (len(bin(i))))
                    print(foo, end="")
                print(bin(i)[2:])
        print()
except EOFError:
    pass
