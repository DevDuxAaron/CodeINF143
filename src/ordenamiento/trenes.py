# def ordenamientoBurbuja(unaLista):
#     global c
#     for numPasada in range(len(unaLista)-1,0,-1):
#         for i in range(numPasada):
#             if unaLista[i]>unaLista[i+1]:
#                 c+=1
#                 temp = unaLista[i]
#                 unaLista[i] = unaLista[i+1]
#                 unaLista[i+1] = temp
#
#
# t=int(input())
# for i in range(t):
#     l=int(input())
#     unaLista = list(map(int,input().split()))
#     c=0
#     ordenamientoBurbuja(unaLista)
#     print(c)

def bubble_sort1(A):
    global c
    for i in range(len(A)-1, 0, -1):
        done = True
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                c += 1
                done = False
        if done:
            return


case = int(input())
for k in range(case):
    n = int(input())
    x = list(map(int, input().split()))
    c = 0
    bubble_sort1(x)
    print(c)
