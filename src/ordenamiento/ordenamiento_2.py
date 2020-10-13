def getkey(item):
    if item[0] == item[0]:
        if item[3] == item[3]:
            return item[4]
        else:
            return item[3]
    else:
        return item[0]


casos = int(input())
m = [["" for i in range(5)] for j in range(casos)]

for i in m:
    print(i)
print()

for i in range(casos):
    x = input()
    for j in range(5):
        m[i][j] = x[j]

for i in m:
    print(i)
print()

m.sort(key=getkey)

for i in m:
    print(i)
