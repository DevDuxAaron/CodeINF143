def bugsito():
    global posibles
    res = []
    for i in posibles:
        if res.count(i) == 0:
            res.append(i)
    posibles = res[:]


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
                continue
            ope[j] = 1
            loop(n, k, pos + 1, ope)
            ope[j] = 0


def show():
    for i in posibles:
        for j in i:
            print(j, end="")
        print()
    print()


x = int(input())
blank = input()
for s in range(x):
    posibles = []
    n, k = map(int, input().split())
    aux = [0 for i in range(n)]
    loop(n, k, 0, aux)
    bugsito()
    posibles.reverse()
    # print(posibles)
    show()
    blank = input()


# def search(i):
#     if len(permutation) == k:
#         foo = permutation[:]
#         posibles.append(foo)
#         for j in range(k):
#             print(permutation[j], end="")
#         print()
#     else:
#         for j in range(i, n):
#             if chosen[j]:
#                 continue
#             chosen[j] = True
#             permutation.append(alfabeto[j])
#             search(j)
#             chosen[j] = False
#             permutation.pop()
#
# alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','r','s','t','u','v','w','x','y','z']
#
# # n = 5
# # k = 3
# n, k = map(int, input().split())
# i = 0
# permutation = []
# chosen = [0] * (n+1)
# posibles = []
# search(i)
# # print(posibles)
