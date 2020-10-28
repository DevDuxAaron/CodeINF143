a = set([])
while True:
    line = input()
    if line == "T":
        break
    if line[0] == "S":
        y, x = line.split()
        # x = int(line[2:])
        a.add(int(x))
    elif len(a) > 0:
        if len(line) == 1:
            if line == "A":
                print(max(a))
            elif line == "R":
                a.remove(max(a))
        else:
            y, x = line.split()
            x = int(x)
            # x = int(line[2:])
            aux = max(a)
            a.remove(aux)
            if line[0] == "D":
                aux -= x
            elif line[0] == "I":
                aux += x
            a.add(aux)
    else:
        print("Error")


# Error
# Error
# 6
# 6
# 4
# -46
# 11
# 11
# Error
# Error
# Error
# Error
# -52
# -52
# -52
# -52
# 7
# Error
# 41
# 81