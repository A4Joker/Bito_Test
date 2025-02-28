from itertools import product

def iter_product():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = sorted(product(a, b))

    for ele in list(c):
        print(ele, end=" ")


iter_product()