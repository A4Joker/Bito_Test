def interchange():

    list1 = [12, 35, 9, 56, 24]
    list2 = []


    first = list1.pop(0)
    last = list1.pop(-1)
    print(first)
    print(last)
    list1.insert(0,last)
    list1.append(first)
    print(list1)

interchange()