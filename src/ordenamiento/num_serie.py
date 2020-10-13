from operator import itemgetter

def same(n):
    i = 0
    c = n[i]
    ini = 0
    foo = len(n)
    for j in range(1, foo):
        sw = False
        b = n[j]
        while len(c) == len(b):
            sw = True
            j += 1
            if j == foo:
                break
            b = n[j]
        if sw:
            fin = j-1
            numero(ini, fin)
        if j == foo:
            break
        i = j
        ini = i
        c = n[i]
        j += 1
        if j == foo:
            break
        b = n[j]


def devolver(ini, fin, s_sumas):
    c = 0
    for i in range(ini, fin+1):
        n[i] = s_sumas[c][0]
        c += 1

def show(cadena):
    for a in cadena:
        print(a, end=" ")
    print()

def numero(ini, fin):
    s_cadena = n[ini:fin+1]
    s_sumas = []
    num = "0123456789"
    for palabra in s_cadena:
        sw_ltr = False
        suma = 0
        conNum = 0
        pri = 0
        for digito in palabra:
            if digito in num:
                suma += int(digito)
                conNum += 1
                if sw_ltr:
                    pri += 1
                    sw_ltr = False
            else:
                sw_ltr = True
        s_sumas.append([palabra, suma, pri, conNum])
    s_sumas.sort(key=itemgetter(1))
    devolver(ini, fin, s_sumas)


while True:
    try:
        n = input().split()
        n.sort(key=lambda item: (len(item), item))
        same(n)
        show(n)
    except EOFError:
        break







# import re

# def getkey(item):
#     return len(item)
#
#
# while True:
#     try:
#         text = input().split()
#         # group_1 = re.findall('[^A-Z]+\s', text)
#         # print(group_1)
#         text.sort(key=getkey)
#         print(text)
#     except EOFError:
#         break