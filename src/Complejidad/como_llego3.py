def NumSteps(P, n):
    count = 0
    i = 0
    while i < n:
        while P[i] != i:
            P[P[i]], P[i] = P[i],  P[P[i]]
            count += 1
        i += 1
    return count


lo = int(input())
x, y = input().split()
P1 = [int(i)-1 for i in x]
P2 = [int(j)-1 for j in y]

P1_inv = [0]*lo
i = 0
while i < lo:
    P1_inv[P1[i]] = i
    i += 1

P = [0]*lo
for i in range(lo):
    P[i] = P2[P1_inv[i]]

num_steps = NumSteps(P, lo)

if num_steps == 0:
    print(num_steps)
else:
    print(num_steps+1)

