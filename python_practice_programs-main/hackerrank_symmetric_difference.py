def set_diff():
    n = int(input())
    a = sorted(list(map(int, input().rstrip().split()))[:n])
    m = int(input())
    b = sorted(list(map(int, input().rstrip().split()))[:m])
    c = set(set(a).difference(set(b)))
    d = set(set(b).difference(set(a)))
    x = c.union(d)
    for ele in sorted(x):
        print(ele,end="\n")


set_diff()
