def listoflist_to_dict():
    list1 = [['a', 'b', '1', '2'], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
    # expected -: {('a', 'b'): (1, 2), ('c', 'd'): (3, 4), ('e', 'f'): (5, 6)}
    dict2 = {(lst[0], lst[1]): tuple(lst[2:]) for lst in list1}
    print(dict2)


listoflist_to_dict()
