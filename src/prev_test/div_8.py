import re

while True:
    try:
        x = input()
        a = "SI" if len(re.findall("[1].*[0].*[0].*[0]", x)) > 0 else "NO"
        print(a)
    except EOFError:
        break
