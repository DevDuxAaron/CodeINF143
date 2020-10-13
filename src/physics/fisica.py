def product_vec(a, b):
    r = [0, 0, 0]
    r[0] = (a[1]*b[2])-(a[2]*b[1])
    r[1] = (a[2]*b[0])-(a[0]*b[2])
    r[2] = (a[0]*b[1])-(a[1]*b[0])
    return r


def show(x):
    aux = ["i", "j", "k"]
    for i in range(3):
        print(str(x[i]) + aux[i], end="\t")
    print()


while True:
    A = list(map(float, input().split()))
    B = list(map(float, input().split()))
    C = list(map(float, input().split()))
    print("V_1 x V_2")
    show(product_vec(A, B))
    print("V_2 x V_1")
    show(product_vec(B, A))
    print("V_3 x V_1")
    show(product_vec(C, A))
    print("V_1 x V_3")
    show(product_vec(A, C))
    print("V_1 x (V_2 x V_3)")
    show(product_vec(A, product_vec(B, C)))
    print("V_3 x (V_2 x V_1)")
    show(product_vec(C, product_vec(B, A)))


# Vector
# 3 4 -5
# 8 5 -6
# -3 -4 5
