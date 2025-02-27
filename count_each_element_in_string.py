def count_each_ele():
    string1 = "tt b a b"
    frequency = dict()
    given_list = [x for x in string1 if x != " "]

    count_list = [(x,given_list.count(x)) for x in given_list]
    print("Count List -:",set(count_list))

    for item in given_list:
        if item not in frequency:
            frequency[item] = 1
        else:
            frequency[item] = frequency[item] + 1

    print(frequency)


count_each_ele()
