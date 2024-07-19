def rem_empty_tuple_from_list():

    t1 = [(), ("ram","15","8"), (), ("laxman", "sita"), ("krishna", "akbar", "45"), (","),()]

    list1 = [x for x in t1 if x != ()]
    print(list1)

rem_empty_tuple_from_list()