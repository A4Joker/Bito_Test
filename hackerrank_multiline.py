if __name__ == "__main__":
    list1 = list()
    try:
        while True:
            line = input()
            if not line:
                break
            list1.append(line)
    except EOFError:
        pass
    print(list1)