A = [0, 9, 2, 4, 1, 5, 3, 7, 5, 1, 0]

for j in range(2, len(A)):
    key = A[j]
    i = j - 1
    while i > 0 and A[i] < key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
print(A)
