def lanzamiento(nivel, indice, c, levels, level, arr):
    if nivel == level:
        levels[nivel][indice] = not levels[nivel][indice]
        arr[indice] = c
        return
    if levels[nivel][indice]:
        levels[nivel][indice] = not levels[nivel][indice]
        lanzamiento(nivel + 1, indice * 2, c, levels, level, arr)
    else:
        levels[nivel][indice] = not levels[nivel][indice]
        lanzamiento(nivel + 1, indice * 2 + 1, c, levels, level, arr)


def get_nivel_X(x):
    arreglo = [0]
    niveles = dict([])
    for ko in range(1, x + 1):
        niveles[ko] = [True] * (2 ** (ko - 1))
    arreglo = [0] * int(2 ** (x - 1))
    for m in range(1, int(2 ** (x - 1)) + 1):
        lanzamiento(1, 0, m, niveles, x, arreglo)
    return arreglo


# print(get_nivel_X(2))
# print(get_nivel_X(3))
# print(get_nivel_X(4))
master = dict([])
for i in range(15, 16):
    master[i] = get_nivel_X(i)
for key, value in master.items():
    print(key, ":", value)

# cases = int(input())
# for _ in range(cases):
#     level, I = map(int, input().split())
#     pos = -1 if I % 2 ** (level - 1) == 0 else I % 2 ** (level - 1)
#     arr = [0] * (2 ** (level - 1))
#     levels = dict([])
#     for k in range(1, level + 1):
#         levels[k] = [True] * (2 ** (k - 1))
#     arr = [0] * (2 ** (level - 1))
#     for i in range(1, (2 ** (level - 1)) + 1):
#         lanzamiento(1, 0, i)
#     aux = tuple(i for i in range(2 ** (level - 1), 2 ** (level - 1) + (2 ** (level - 1))))
#     try:
#         if pos != -1:
#             res = arr.index(pos)
#             print(aux[res])
#         else:
#             print(aux[pos])
#     except ValueError:
#         # print(len(arr))
#         print(min(arr), max(arr))
#         print(pos)
#         print(aux.index(max(aux)))
#         print(aux)

    # # fun(1, len(arr), 1,)
    # for k in range(1,20):
    #
    #     print(aux)
