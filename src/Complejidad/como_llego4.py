def move(x, y):
    global c
    for i in range(x - y):
        ini_aux[x], ini_aux[x-1] = ini_aux[x-1], ini_aux[x]
        x -= 1
        c += 1
        # print(ini_aux)


n = int(input())
ini, fin = input().split()
c = 0
ini_aux = [i for i in ini]
for i in range(len(fin)):
    act = fin[i]
    pos_ori = ini_aux.index(act)
    move(pos_ori, i)
if c == 0:
    print(c)
else:
    print(c+1)
