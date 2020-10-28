t = int(input())
for _ in range(t):
    line = input()
    aux = dict([])
    for i in range(len(line)):
        if line[i] != " ":
            try:
                aux[line[i]] += 1
            except KeyError:
                aux[line[i]] = 1
    if len(set(aux.values())) == 1:
        print("No te lo tomes enserio")
    else:
        print("Meh")
