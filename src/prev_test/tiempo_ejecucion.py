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
    r = ""
    aux = stack.pop(0)
    while len(stack) > 0:
        aux_2 = stack.pop(0)
        if aux == "for" and aux_2 == "for":
            r += "n("
        elif aux == "for" and aux_2 == "end":
            r += "n"
        elif aux == "for" and aux_2 == "ope":
            r += "n(1"
        elif aux == "end" and aux_2 == "for":
            r += "+"
        elif aux == "end" and aux_2 == "ope":
            r += "+1"
        elif aux == "ope" and aux_2 == "for":
            r += "+1+"#
        elif aux == "ope" and aux_2 == "end":
            r += ")"
        elif aux == "ope" and aux_2 == "ope":
            r += "+1"
        elif aux == "end" and aux_2 == "end":
            r += ")"
        aux = aux_2
    if lines == 1:
        r += "1"
    if r[0] == "+":
        r = r[1:]
    r = "T(" + r + ")"
    print(r)

# T(1+n+n(n(1)+1)+n(n(1)+1+n+1)+1+n)
# T(1+1+n+n(n(1)+1)+n(n(1)+1  +n+1)+1+n+1+1+1+n(n(1+n+n(1+n(1)))
# T(1+1+n+n(n(1)+1)+n(n(1)+1+1+n+1)+1+1+n)
# T(1+1+n+n(n(1)+1)+n(n(1)+1+1+n+1)+1+1+n)
