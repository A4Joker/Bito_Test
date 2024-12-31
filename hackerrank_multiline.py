if __name__ == "__main__":
    input_lines = list()
    try:
        while True:
            line = input()
            if not line:
                break
            list1.append(line)
    except EOFError:
        print("Reached end of input")
    print(list1)