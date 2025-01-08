def even_len(given_string):
    if not isinstance(given_string, str):
        raise TypeError("Input must be a string")
    if not given_string.strip():
        return []
    given_list = given_string.split()
    list2 = list()
    print("given list -:", given_list)
    for ele in given_list:
        if len(ele) % 2 ==0:
            list2.append(ele)
    print(" ".join(list2))


even_len("your string here")