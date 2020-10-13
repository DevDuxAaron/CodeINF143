def getKey(item):
    return item[1]


pro = dict([])
while True:
    try:
        res = input().split()
        if len(res) == 2:
            if res[1] in pro:
                pro[res[1]] += 2
            else:
                pro[res[1]] = 2
        elif len(res) == 3:
            if res[1] in pro:
                pro[res[1]] += 1
            else:
                pro[res[1]] = 1

            if res[2] in pro:
                pro[res[2]] += 1
            else:
                pro[res[2]] = 1
    except EOFError:
        break

x = max([key for key in pro.keys()])
res = []
for key, value in pro.items():
    res.append([key, value])
res.sort(reverse=True, key=getKey)
aux = dict([])
for i in res:
    if i[1] in aux:
        aux[i[1]].append(i[0])
    else:
        aux[i[1]] = [i[0]]
for k, v in aux.items():
    for i in sorted(v):
        print(i, k)
