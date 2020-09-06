# def funar(ini, fin):
#     global res
#     for k in range(ini, fin):
#         res ^= elem[k]
#
# def subconjunto(k):
#     for i in range(n-k+1):
#         funar(i, i+k)
#
# def love(foo):
#     for h in range(1, n+1):
#         subconjunto(h)
#
#
# casos = int(input())
# for i in range(casos):
#     res = 0
#     n = int(input())
#     elem = list(map(int, input().split()))
#     elem.sort()
#     elem = {x: elem[x] for x in range(n)}
#     love(elem)
#     print(res)


import sys

def xor(conj, aux):
    if aux % 2 == 0:
        return 0
    res = 0
    for i in range(0, aux, 2):
        res ^= conj[i]
    return res


enter = sys.stdin
n = int(enter.readline())
for k in range(n):
    a = int(enter.readline())
    x = [int(x) for x in input().split()]
    print(xor(x, a))
