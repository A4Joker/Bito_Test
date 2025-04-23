if __name__ == "__main__":
    input_lines = list()
    try:
        while True:
            line = input()
            if not line.strip():
                break
            input_lines.append(line)
    except EOFError:
        print("Reached end of input")