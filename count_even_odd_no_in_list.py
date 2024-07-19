def even_odd_list():
    list1 = [2, 7, 7, 5, 64, 64, 14]
    count_even = 0
    count_odd = 0
    for ele in list1:
        if ele % 2 == 0:

            count_even += 1

        else:

            count_odd += 1

    print(count_even, count_odd)


even_odd_list()
