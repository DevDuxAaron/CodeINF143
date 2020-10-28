import math

def isPrime(n):
    if n <= 1:
        return False
    else:
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                return False
    return True

def primeFactors(x):
    if isPrime(x):
        return x
    p = 0
    value = x
    for k in range(2, math.floor(x / 2) + 1):
        if isPrime(k):
            while value % k == 0:
                value = value / k
                p += k
    return p


t = int(input())
for i in range(t):
    num = int(input())
    if isPrime(primeFactors(num)):
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
