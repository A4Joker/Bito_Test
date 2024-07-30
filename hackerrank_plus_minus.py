def plus_minus():
    list1 = [-4, 3, -9, 0, 4, 1]
    positive_counter = 0
    negative_counter = 0
    zero_counter = 0
    positive_ratio = 0
    negative_ratio = 0

    for ele in list1:
        if ele > 0:
            positive_counter += 1
        elif ele < 0:
            negative_counter += 1
        else:
            zero_counter += 1

    print(positive_counter,negative_counter,zero_counter)
    positive_ratio = float(positive_counter/len(list1))
    negative_ratio = float(negative_counter/len(list1))
    zero_ratio = float(zero_counter/len(list1))
    print(float(positive_ratio))
    print(round(negative_ratio,6))
    print(round(zero_ratio,6))
plus_minus()
