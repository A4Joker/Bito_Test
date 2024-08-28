def remove_empty_list():


    list1 = [1,42,4,6,[1],4,[],[],[1],[]]
    print(list1)

    list2 = [ x for x in list1 if x != []]
    prin(list2)
remove_empty_list()