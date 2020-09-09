def move(x, y):
    global c
    for i in range(x, y):
        c += 1
        aux[i], aux[i+1] = aux[i+1], aux[i]


n = int(float(input()))
ini, fin = input().split()
c = 1
j = 0
aux = [i for i in ini]
res = fin
while fin != "".join(aux):
    src = j
    dest = fin.index(aux[j])
    move(src, dest)
    j += 1
    if j >= n:
        j = 0
print(c)

# 1
# 1 1
# Res 1
#
# 3
# 120 102
# Res 2
#
# 3
# 201 102
# Res 4
