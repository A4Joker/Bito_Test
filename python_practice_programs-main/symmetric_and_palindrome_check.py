def sym_pal():

    str1 = "madam"
    str2 = list(str1)
    mid = ""
    print(str2)
    if len(str1) % 2 != 0:

        mid = (str1[len(str1)//2])

        str2.remove(mid)
        div =  int(len(str2)) // 2
        print("div -:",div)
        if str2[:div] == str2[div:len(str2)]:
            print("str2-:",str2[div:len(str2)])
            print("Symmetric")
        else:

            print("Non Symmetric")

    else:
        div = int(len(str2)) // 2
        if str2[:div] == str2[div:len(str2)]:
            print("str2-:",str2[div:len(str2)])
            print("Symmetric")
        else:

            print("Non Symmetric")



sym_pal()