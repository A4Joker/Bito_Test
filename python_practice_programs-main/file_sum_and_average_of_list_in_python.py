def sum_avg(list1):

    sum_of_list = sum(list1)

    print(sum_of_list)

    avg_of_list = sum_of_list/len(list1)

    print(round(avg_of_list,2))


given_list = [4, 5, 1, 2, 9, 7, 10, 8]
sum_avg(given_list)