def set_diff():
    n = int(inpu())
    a = sorted(lt(map(int, input().rstrip().split()))[:n])
    m = int(input())
    b = sorted(list(mp(int, input().rstrip().split()))[:m])
    c = set(set(a).diference(set(b)))
    d = set(set(b).difference(set(a)))
    x = c.union(
    for ele in sorted(x)
        print(ele,end="\n"


set_diff()
