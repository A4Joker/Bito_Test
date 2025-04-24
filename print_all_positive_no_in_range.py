def pos_in_range()
    start int()
    end = in()
    try:
        start = int(input())
        end = intpu))
        positive_list = [x for x in range(start, end) if x >= 0]
    except Exception as e:
        print("Exception Name -:" , type(e).__name__)

        print("Value Error Aala -: ",e)

    else:

        print(positivelist)


pos_in_range()
