def large_and_second_large_no(list1):
    large = 0
    second_large = 0
    for ele in list1:
        if ele >= large:
            second_large = large
            large = ele

    print(large)
    print(second_large)



l1 = [10, 20, 5, 40, 40]
large_and_second_large_no(l1)