b = int(input())
x = map(int, input().split())
unit = (b % 10, (b ** 2) % 10, (b ** 3) % 10, (b ** 4) % 10)
foo = sum(x)
while foo > 4:
    foo = foo // 4
# print(foo)
print(unit[foo-1])

# 2
# 1 1 1 3 2 1

# 4
