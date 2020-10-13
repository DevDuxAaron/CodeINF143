t = int(input())
for i in range(t):
    step, ini = map(int, input().split())
    cont = 1
    sign = 1
    aux = 0
    r = ""
    for j in range(step):
        r += str(ini) + " "
        if aux == cont:
            sign *= -1
            aux = 0
            cont += 1
        ini += sign
        aux += 1
    print(r[:-1])
