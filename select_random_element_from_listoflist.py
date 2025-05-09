import random
from random import randint
def rand_listoflist():
    given_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

    flatten_list = [ele for sublist in given_list for ele in sublist]

    print("Using list comprehension-:\t",flatten_list)

    flatten_list1 = list()

    for sublist in given_list:
        for ele in sublist:
            flatten_list1.append(ele)
    print("Using traditional for loop-:\t",flatten_list1)

    # now print random element from list
    ran_int = random.randint(0,len(flatten_list1)-1)
    print("Random index -:",ran_int)
    random_ele = flatten_list[ran_int]
    print(f"Random Element -: \t{random_ele} \t at Index -: {ran_int}")

rand_listoflist()