# n = int(input())
# my = dict([])
# for i in range(n):
#     y = input()
#     my[y] = input()
# x = int(input())
# for i in range(x):
#     y = input()
#     print(my[y])


def long(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


x = list(map(float, input().split()))
a, b, c = long(x[0], x[1], x[2], x[3]), long(x[0], x[1], x[4], x[5]), long(x[4], x[5], x[2], x[3])
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(round(area, 1))
