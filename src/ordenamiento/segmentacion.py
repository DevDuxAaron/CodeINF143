def getKey(item):
    return item[0]


while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        pro = [[a[i], b[i]] for i in range(n)]
        pro.sort(key=getKey)
        aux = [0] * (max(b) + 1)
        for i in pro:
            for j in range(i[0], i[1]):
                aux[j] = 1
        print(aux.count(1))
    except EOFError:
        break
        # s = 0
        # for i in range(len(aux)):
        #     if aux[i] == 1:
        #         s += 1
        # print(s)

        # i = 0
        # ope = pro.pop(0)
        # while len(pro) > 1:
        #     sig = pro.pop(0)
        #     if ope[1] < sig[0]:
        #         s += abs(ope[0] - ope[1])
        #         ope = sig[:]
        #     elif ope[1] >= sig[1]:
        #         s += abs(ope[0] - ope[1])
        #         ope = pro.pop(0)
        #     elif sig[1] > ope[0]:
        #         s += abs(ope[0] - sig[1])
        #
        # s = 0
        # i = 0
        # while len(pro) >= 2:
        #     aux_1 = pro[0]
        #     aux_2 = pro[1]
        #     if aux_2[0] < aux_1[1] <= aux_2[1]:
        #         s += abs(aux_1[0] - aux_2[1])
        #         aux = pro.pop(0)
        #         foo = pro.pop(0)
        #     elif aux_1[1] > aux_2[1]:
        #         s += abs(aux_1[0] - aux_1[1])
        #         aux = pro.pop(0)
        #         foo = pro.pop(0)
        #     else:
        #         s += abs(aux_1[0] - aux_1[1])
        #         foo = pro.pop(0)
        # if len(pro) == 1:
        #     s += abs(pro[0][0] - pro[0][1])
        # print(s)
    except EOFError:
        break
