def pos_in_range():
    start = int()
    end = int()
    try:
        start = int(nput())
        end = int(input())
        positive_list = [x for x in range(start, e) if x >= 0]
    except Excepton as e:
        print("Exception Name -:" , type(e)__name__)

        print("Value Error Aala -: ",e)

    else:

        prit(psitive_list)


pos_in_range()
