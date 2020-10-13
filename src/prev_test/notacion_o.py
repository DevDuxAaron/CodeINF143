prog = int(input())
for i in range(prog):
    lines = int(input())
    stack = []
    for j in range(lines):
        line = input()
        if "for" in line:
            stack.append("for")
        elif "}" in line:
            stack.append("end")
        else:
            stack.append("ope")
    aux = stack.pop(0)
    c = 0
    lin = 0
    while len(stack) > 0:
        aux_2 = stack.pop(0)
        if aux == "for" and aux_2 == "for":
            c += 1
        elif aux == "for" and aux_2 == "end":
            lin = 1
        elif aux == "ope" and aux_2 == "end":
            lin = 1
        aux = aux_2
    if c == 0 and lin == 0:
        print("O(1)")
    elif c >= lin:
        c += 1
        print("O(n^{})".format(c))
    else:
        print("O(n^{})".format(lin))
