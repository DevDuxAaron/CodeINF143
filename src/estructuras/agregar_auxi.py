import sys
import heapq

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    B = [int(i) for i in input().split()]
    A = []
    for i in B:
        heapq.heappush(A, i)
    res = 0
    while len(A) > 1:
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        a = a + b
        res += a
        A.append(a)
    print(res)
