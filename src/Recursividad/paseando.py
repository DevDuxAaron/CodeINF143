def show():
    for i in matrix:
        print(i)
    # print(x, y)
    print()

def let(i, j):
    if fil > i > -1 and -1 < j < col:
        return matrix[i][j] != '2' and matrix[i][j] != '3' and (matrix[i][j] == '0' or matrix[i][j] == '1')
    else:
        return False

def move(x, y):
    global c
    # print(x, y)
    # show()
    if let(x, y+1):
        c+=1
        matrix[x][y+1] = '3'
        move(x, y+1)
    if let(x, y-1):
        c += 1
        matrix[x][y-1] = '3'
        move(x, y-1)
    if let(x+1, y):
        c += 1
        matrix[x+1][y] = '3'
        move(x+1, y)
    if let(x-1, y):
        c += 1
        matrix[x-1][y] = '3'
        move(x-1, y)
    return


fil, col = map(int, input().split())
while fil != 0 and col != 0:
    c = 0
    matrix = [[0 for i in range(col)] for k in range(fil)]
    x, y = 0, 0
    for i in range(fil):
        line = input()
        line = line.replace(".", "0")
        line = line.replace("#", "2")
        if line.count('@') == 1:
            x = i
            y = line.index("@")
            line = line.replace('@', '1')
        for m in range(col):
            matrix[i][m] = line[m]
    move(x, y)
    print(c)
    fil, col = map(int, input().split())
