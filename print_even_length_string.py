def even_len():
    given_string = "This is a python language"
    given_list = given_string.split()
    list2 = list()
    print("given list -:", given_list)
    for ele in given_list:
        if len(ele) % 2 ==0:
            list2.append(ele)
    print(" ".join(list2))


even_len()