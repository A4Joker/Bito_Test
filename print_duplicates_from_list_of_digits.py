def dupl():

    list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
    dupl = dict()
    duplicate = []

    list2 = set([x for x in list1 if list1.count(x) > 1])
    list3 = {x: list1.count(x) for x in list1}
    print("Count in List Comprehension-:",list3)
    print("List Comprehension of duplicate-:", list2)
    for ele in list1:
        if ele in dupl:
            dupl[ele] = dupl[ele] + 1
        else:
            dupl[ele] = 1
    print(dupl)
    for key, value in dupl.items():
        if value > 1:
            duplicate.append(key)
        else:
            continue
    print(duplicate)
dupl()