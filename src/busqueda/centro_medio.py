# while True:
#     try:
#         n = int(input())
#         aux = n // 4
#         m = n // 2
#         if n <= 3:
#             print("NO")
#         while m > 1:
#             a = ((m-1)*((m-1)+1))//2
#             b = ((n*(n+1))//2) - a - m
#             if a == b:
#                 print(m)
#                 break
#             elif a > b:
#                 print("NO")
#                 break
#             else:
#                 m = m + aux
#                 aux //= 2
#     except EOFError:
#         break

def centroMedio(n):
    global c
    a = 1
    b = n-1
    sw = False
    while a <= b:
        c = (a+b)//2
        sMenor = (c - 1) * (c) // 2
        sMayor = gen - c - sMenor
        if sMenor == sMayor:
            r = 1
        else:
            if sMayor > sMenor:
                r = 2
            else:
                r = 3
        if r == 1:
            sw = True
            break
        elif r == 2:
            a = c+1
        else:
            b = c-1
    if sw:
        print(c)
    else:
        print("NO")


while True:
    try:
        n = int(input())
        if n == 1:
            print(n)
        else:
            gen = n * (n + 1) // 2
            centroMedio(n)
    except EOFError:
        break
