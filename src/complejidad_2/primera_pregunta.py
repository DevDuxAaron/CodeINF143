import math
x = int(input())
for i in range(x):
    a, b = map(int, input().split())
    print(int(b**0.5) - math.ceil(a**0.5) + 1)
# if a**0.5 != int(a**0.5):
#     print(int(b**0.5) - int(a*0.5))
# else:
#     print(int(b**0.5) - int(a**0.5)+1)
