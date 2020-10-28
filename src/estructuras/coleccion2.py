def operSumRes(opc, x, line):
    if len(line) > 0:
        mayor = max(line)
        line.remove(mayor)
        if opc == "D":
            mayor -= x
        else:
            mayor += x
        line.append(mayor)
    else:
        print("Error")


def borrar(line):
    if len(line) > 0:
        line.remove(max(line))
    else:
        print("Error")


def show(line):
    if len(line) > 0:
        print(max(line))
    else:
        print("Error")


def opciones(opc, line):
    if len(opc) == 1:
        if opc == "R":
            borrar(line)
        if opc == "A":
            show(line)
    else:
        lr = opc.split()
        x = lr[0]
        y = lr[1]
        if x == "S":
            line.append(int(y))
        else:
            operSumRes(x, int(y), line)


line = []
while True:
    try:
        opc = input()
        if opc == "T":
            break
        opciones(opc, line)
    except EOFError:
        break
