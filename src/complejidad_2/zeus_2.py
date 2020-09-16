def show(foo):
    res = ""
    for k in foo:
        res += ("R" if k else "Z") + " "
    return res


monedas, ope = map(int, input().split())

money = [0] * monedas
for i in range(ope):
    # print(money)
    x, y = map(int, input().split())
    for j in range(x - 1, y):
        if money[j] == 1:
            money[j] = 0
        else:
            money[j] = 1
print(show(money))
