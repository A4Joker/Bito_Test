def mul_digits(list1):
    result = int(1)
    for ele in list1:
        if ele.isdigit():

            result = int(ele) * result
        continue
    print(result)




l1 = ["3","Z","A", "2", "4"]
mul_digits(l1)