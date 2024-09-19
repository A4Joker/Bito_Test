def rem_list_ele():
    given_list = [12, 15, 3, 10]
    remove_list = [12,3]
    new_list = [ele for ele in given_list if ele not in remove_list]


    print(new_list)


rem_list_ele()