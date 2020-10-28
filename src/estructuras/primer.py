import re

line_aux = []
while True:
    try:
        line = input()
        line = line.lower()
        if len(line) != 0:
            line_aux.extend(re.findall("[a-zA-z]+", line))
        if line == "zorro":
            break
    except EOFError:
        break
try:
    line_aux = list(set(line_aux))
    line_aux.sort()
    for _ in line_aux:
        print(_)
except Exception:
    pass

