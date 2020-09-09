import unittest


def fun(n, k):
    if k < (n // 2):
        for j in range(n - 2):
            if (j * 2) + 1 >= k:
                return j
    else:
        for j in range(n - 2, 0, -1):
            if (j * 2) <= k:
                return j


class FunBlackBox(unittest.TestCase):
    def test_case_1(self):
        n1 = 11864
        n2 = 9862
        res = fun(n1, n2)
        self.assertEqual(res, 1002)

    def test_case_2(self):
        n1 = 6454
        n2 = 5016
        res = fun(n1, n2)
        self.assertEqual(res, 720)

    def test_case_3(self):
        n1 = 17900
        n2 = 1054
        res = fun(n1, n2)
        self.assertEqual(res, 528)

    def test_case_4(self):
        n1 = 16478
        n2 = 8252
        res = fun(n1, n2)
        self.assertEqual(res, 1252)

    def test_case_5(self):
        n1 = 5322
        n2 = 268
        res = fun(n1, n2)
        self.assertEqual(res, 4114)


# case = int(input())
# for i in range(case):
#     n, k = map(int, input().split())
#     print(fun(n, k))

if __name__ == '__main__':
    unittest.main()

# 1000
# 11864 9862
# 6454 5016
# 17900 1054
# 7088 4587
# 16478 8252
# 5322 268
#
# 1002
# 720
# 528
# 1252
# 4114
