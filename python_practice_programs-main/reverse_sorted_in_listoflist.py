def rev_sort():

    given_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

    rev_sorted_list = [sorted(ele,reverse=True) for ele in given_list]
    print(rev_sorted_list)
    rev_sorted_list1= list()
    for ele in given_list:
        ele.sort(reverse=True)
    print(given_list)
rev_sort()