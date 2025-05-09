def rev_words():

    given_string = " geeks quiz practice code"
    list_of_string = list(given_string.split())
    print("Given String -:",list_of_string)
    str2 = ""
    #rev_list = list_of_string[::-1]
    rev_list = list()
    size = (len(list_of_string))
    for ele in range(size-1,-1,-1):
        #print("-ele -:", ele,end=" ")
        rev_list.append(list_of_string[ele])
        #print("from here")
    print(rev_list)



rev_words()