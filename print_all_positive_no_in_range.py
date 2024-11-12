def pos_in_range():
    start = int()
    end = int()
    try:
        start = int(input())
        end = int(input())
        positive_list = [x for x in range(start, end) if x >= 0]
    except Exception as e:
        print("Exception Name -:" , type(e).__name__)

        print("Value Error Aala -: ",e)

    else:

        print(positive_list)


pos_in_range()
