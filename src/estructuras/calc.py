while True:
    try:
        line = input().split(",")
        price = 0
        win = 0
        for k in line:
            aux = k.split()
            price += float(aux[0])
            win += float(aux[0]) - float(aux[1])
        res = int((win/price)*100)
        print(res)
    except EOFError:
        break
