# x = ("942", "192", "442", "692", "942")
# casos = int(input())
# for k in range(casos):
#     n = int(input())
#     ad = (str((n - 1) // 4) if n > 4 else "") + x[n % 4]
#     print(ad)

x = ("942", "192", "442", "692", "942")
casos = int(input())
for k in range(casos):
    n = int(input())
    print(192 + (250 * (n - 1)))

i = 1
j = 0
r = []
while True:
    i += 1
    if (i * i * i)%1000 == 888:
        r.append(i)
        j += 1
    if j == 10:
        break
print(r)
for i in range(1, len(r)):
    print(r[i]-r[i-1], end=" ")

# 6291192
# 5512942
# 2262692
# 3339692
# 13692
# 2608942
# 3112442
# 6024942
# 6734942
# 2323692
# 5660442
# 5928692
# 3852442
# 3028942
# 6011192
# 4213692
# 7161942
# 1885692
# 6013692
# 3048692
# 7490442
# 5744692
# 2062942
# 7460192
# 3024942
# 720442
# 7772942
# 7490942
# 618442
# 6642692
# 2233442
# 3379942
# 2709942
# 2630942
# 2762442
# 1319442
# 597192
# 5642192
# 6412942
# 1548942
# 7087442
# 6316692
# 7331442
# 4638942
# 1799942
# 3014692
# 6265192
# 384942
# 2377192
# 2206