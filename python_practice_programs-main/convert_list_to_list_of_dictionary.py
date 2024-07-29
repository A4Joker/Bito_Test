def list_of_dict():
    given_list = [["Akshay", 3, "Rekha", 8, "Rajendra", 6], ["name", "id"]]

    key_list = given_list[-1]
    value_list = list()
    dict1 = {}
    print("key list -:",key_list)
    for ele1 in range(0, len(given_list) - 1):
        for ele2 in given_list[ele1]:
            value_list.append(ele2)
    print("value list -:", value_list)
    print("hello")
    dict1 = dict(zip(key_list,value_list))
    for key, value in dict1.items():
        print(key,value)
list_of_dict()
