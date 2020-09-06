# def factorial (n, a=1) :
#     if n == 0:
#         return a
#     return factorial(n-1,n*a)


# sw = True
# while sw:
#     a,b = map(int,input().split())
#     if a == b == 0:
#         break
#     print( int((factorial(a+b))/(factorial(a)*factorial(b))) )

# Globals
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

def loop(n, k, pos, ope):
    global posibles
    # print(n, k, pos, ope)
    if ope.count(1) == k:
        foo = ope[:]
        posibles.append(foo)
        return
    else:
        for j in range(pos, n):
            if ope[j]:
                print('NO es en vano')
                continue
            ope[j] = 1
            loop(n, k, pos + 1, ope)
            ope[j] = 0


def loopy(pos, ope):
    if ope.count(1) == k:
        # for j in ope:
        #     print(j, end="")
        print(ope)
    else:
        for i in range(pos, n):
            if ope[i]:
                continue
            ope[i] = 1
            loopy(pos+1, ope)
            ope[i] = 0


while True:
    try:
        # n, k = map(int, input().split())
        n, k = 3, 2
        aux = [0]*n
        loopy(0, aux)
        break
    except EOFError:
        break
