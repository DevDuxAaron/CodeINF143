def fun(ini, fin, din):
    global x
    mid = len(din)//2
    if len(din) == 2 or len(din) == 1:
        return din[0]
    elif x > dinos[mid]:
        fun(mid+1, fin, din[mid+1:fin+1])
    elif x < dinos[mid]:
        fun(0, mid, din[0:mid])


n_dinos = int(input())
dinos = [0] * 101
for i in range(n_dinos):
    dinos[int(input())] += 1
# print(dinos)
rondas = int(input())
for j in range(rondas):
    x = int(input())
    s = sum(dinos[:x + 1])
    k = 0
    for i in range(1, x+1):
        k += i * dinos[i]
    print(s, k)


# n_dinos = int(input())
# dinos = [0]*(n_dinos + 1)
# for i in range(n_dinos):
#     dinos[i] = int(input())
# dinos.sort()
# rondas = int(input())
# su = {0: 0}
# for j in range(rondas):
#     x = int(input())
#     s = 0
#     k = 0
#     if x in su:
#         print(su[x][0], su[x][1])
#     else:
#         while k < len(dinos):
#             if dinos[k] <= x:
#                 su[k] = [k, s]
#                 s += dinos[k]
#             if dinos[k] > x:
#                 break
#             k += 1
#         print(k, s)

    # y = fun(0, len(dinos) - 1, dinos)
    # print(dinos.index(y) + 1, sum(dinos[:dinos.index(y) + 1]))


    # if x in dinos:
    #     print(dinos.index(x)+1, sum(dinos[:dinos.index(x)+1]))
    # else:
    #     if x > dinos[-1]:
    #         print(n_dinos, sum(dinos))
    #     else:
    #         x = fun(0, len(dinos) - 1, dinos)
    #         print(dinos.index(x)+1, sum(dinos[:dinos.index(x)+1]))