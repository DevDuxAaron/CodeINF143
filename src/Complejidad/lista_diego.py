# def num1():
#     aux = 0
#     while True:
#         aux += x
#         yield aux
#
# def num2():
#     aux = 0
#     while True:
#         aux += y
#         yield aux
#
#
# x, y, p = 1598, 4196, 278615#map(int, input().split())
# c = 0
# n1 = num1()
# n2 = num2()
# aux_1 = next(n1)
# aux_2 = next(n2)
# if p > 2:
#     if x == y:
#         for i in range(p-1):
#             c = next(n1)
#     else:
#         for i in range(p+96):
#             if aux_1 == aux_2:
#                 if x < y:
#                     aux_1 = next(n1)
#                 else:
#                     aux_2 = next(n2)
#             else:
#                 if aux_1 < aux_2:
#                     c = aux_1
#                     aux_1 = next(n1)
#                 else:
#                     c = aux_2
#                     aux_2 = next(n2)
#     print(c)
# elif p == 1:
#     print(min(aux_1, aux_2))
# elif p == 2:
#     print(max(aux_1, aux_2))

# Problem: 1836
#     User: joel4254
#     Language: Python3.7
#     Result: Accepted
#     Time:292 ms
#     Memory:32164 kb


