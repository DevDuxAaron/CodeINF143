ciclos = (
    (0, 0, 0, 0),
    (1, 1, 1, 1),
    (2, 4, 6, 8),
    (3, 9, 7, 1),
    (4, 6, 4, 6),
    (5, 5, 5, 5),
    (6, 6, 6, 6),
    (7, 9, 3, 1),
    (8, 4, 2, 6),
    (9, 1, 9, 1)
)

b = int(input())
x = list(map(int, input().split()))

foo = 1
for i in range(len(x)):
    foo *= x[i]
print((b**foo) % 10)
# unit = (b % 10, (b ** 2) % 10, (b ** 3) % 10, (b ** 4) % 10)
# foo = sum(x)
# print(ciclos[b][foo % 4])
# print(foo)

# if b == 2:
#     foo = foo % 4
#     print(ciclos[b][foo])
# elif b == 0 or b == 1 or b == 5 or b == 6:
#     print(b)
# elif b == 9 or b == 4:
#     if foo % 2 == 0:
#         print(ciclos[b][1])
#     else:
#         print(ciclos[b][0])
# else:
#     foo = foo % b
#     print(unit[foo])
# if b % 2 == 0:
#     foo = foo % 4
# else:
#     foo = foo % b
# print(foo)
# print(unit)
# try:
#     print(unit[foo])
# except IndexError as e:
#     print(foo)
#     print(unit)
#     print(e)

# 2
# 1 1 1 3 2 1

# 4

# 3
# 1 1 1 3 2 2

# 1

# 5
# 1 1 1 3 2 1

# 5