cases = int(input())
pro = dict([])
for i in range(cases):
    res = input().split()
    foo = int(res[0])
    aux = ord(res[1][-1])
    if foo in pro:
        # pro[foo][aux - 97] += 1
        pro[foo][aux] += 1
    else:
        pro[foo] = dict([])
        pro[foo][aux] = 1
        # pro[foo] = [0]*26
        # pro[foo][aux - 97] = 1

for i in pro.keys():
    for j in range(25, -1, -1):
        if pro[i][j] != 0:
            aux = str(i) + " $" + chr(j) + "\n"
            # aux = str(i) + " $" + chr(j + 97) + "\n"
            print(aux * pro[i][j], end="")

            # for k in range(pro[i][j]):
            #     print(i, "$"+chr(j+97))





# for i in range(1, 101):
#     pro[i].sort(reverse=True)
#
# for i in range(1, 101):
#     for j in pro[i]:
#         if j != "":
#             print(i, j)
