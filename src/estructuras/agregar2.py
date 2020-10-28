n = 2
while n != 0:
    n = int(input())
    if n == 0:
        break
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums)
    res = []
    x = 0
    s = nums.pop(0)
    for i in range(n-1):
        s += nums[0]
        x = nums.pop(0)
        res.append(s)
        print(s, end=" ")
    print()
    print(sum(res))

# 6
# 297 371 635 792 62
# answer: 6621
# 1163 1225 1522 2131 2766
# 671 968 1339 1974 2766
