# not optimized, equiv to while version below, but uses for loop


def insertion_sort1(A):
    global c
    for i in range(1, len(A)):
        for j in range(i - 1, -1, -1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                c += 1
            else:
                break


while True:
    try:
        A = list(map(int, input().split()))
        c = 0
        insertion_sort1(A)
        print(c)
    except EOFError:
        break

# A = [5, 9, 1, 2, 4, 8, 6, 3, 7]
# A = [20, 40, 30, 10]
# A = [-1, 1, 0]
# A = [-1000, 0, 1000]
# print(A)
# c = 0
# insertion_sort1(A)
# print(A)
# print(c)
