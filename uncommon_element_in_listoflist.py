def uncommon_in_listoflist():

    list1 = [[1, 2], [3, 4], [5, 6]]
    list2 = [[3, 4], [5, 7], [1, 2]]
    #expected list [[5, 6], [5, 7]]
    list3 = list()
    list4 = [ele1 for ele1 in list1 if ele1 not in list2]+[ele2 for ele2 in list2 if ele2 not in list1]
    print("list4 -:",list4)
    for ele1 in list1:
        if ele1 not in list2:
            list3.append(ele1)
    for ele2 in list2:
        if ele2 not in list1:
            list3.append(ele2)
    print(list3)


uncommon_in_listoflist()