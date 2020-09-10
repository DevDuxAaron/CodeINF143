# import unittest

# class BlackBox(unittest.TestCase):
#     def test_pato(self):
#         x = 321
#         y = 213
#         result = move(x, y)
#         self.assertEqual(result, 3)


def move(i, j):
    global c
    c += j - i
    for k in range(i, j):
        extra[k], extra[k + 1] = extra[k + 1], extra[k]

# def move(x, y):
#     return None


# if __name__ == "__main__":
n = 8 #int(input())
ini, fin = "12345678", "87654321" #input().split()
c = 0
if ini == fin:
    print(c)
else:
    aux = ini
    src = 0
    while aux != fin and src < n:
        extra = [i for i in aux]
        dest = fin.index(aux[src])
        if src != dest:
            move(src, dest)
        aux = "".join(extra)
        src += 1
    print(c)