def search(y):
    global count
    if y == n:
        if col[x1-1] == y1 or col[x2-1] == y2 or col[x3-1] == y3 or col[x4-1] == y4:
            count += 1
    else:
        for x in range(n):
            if col[x] or diag1[x+y] or diag2[(x-y+n-1)]:
                continue
            col[x] = y+1
            diag1[x+y] = 1
            diag2[(x-y+n-1)] = 1
            search(y+1)
            col[x] = diag1[x+y] = diag2[(x-y+n-1)] = 0


n = 8

N = n*2-1
col = [0] * (n)
diag1 =[0] * (N)
diag2 =[0] * (N)
t = int(input())
for i in range(t):
    count = 0
    x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    search(0)
    print(92-count)