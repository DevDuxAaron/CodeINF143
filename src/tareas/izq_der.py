x = input().split()
aux = dict([])
for i in range(len(x)):
    try:
        aux.pop(x[i])
    except KeyError:
        aux[x[i]] = 1
foo = len(aux)//2
print(len(aux) - foo, foo)
