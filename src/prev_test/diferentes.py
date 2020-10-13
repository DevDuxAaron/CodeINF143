# while True:
#     try:
#         n = int(input())
#         x = input().split()
#         q = int(input())
#         for i in range(q):
#             s = 0
#             a, b = map(int, input().split())
#             aux = []
#             for j in range(a-1, b):
#                 if not x[j] in aux:
#                     aux.append(x[j])
#             print(len(aux))
#     except EOFError:
#         break

def sumar_digitos(x):
    si = 0
    while x > 0:
        d = x % 10
        x = x // 10
        si += d
    return si


v = [0] * 10010
while True:
    try:
        n, a, b = map(int, input().split())
        c = 0
        suma = 0
        for i in range(1, n+1):
            if i > 9:
                v[c] = sumar_digitos(i)
            else:
                v[c] = i
            if a <= v[c] <= b:
                suma += i
            c += 1
        print(suma)
    except EOFError:
        break
