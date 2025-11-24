def rev(sentence):
    S1 = sentence.split()
    rev_list = S1[::-1]
    final_rev = []
    final_words = ""
    swap_case_chars = ""
    print("rev list -:",rev_list)
    final_words = " ".join(rev_list)
    print("final words -:",final_words)
    for words in final_words:

        for char in words:
            if char.isspace():
                print("here is space")
                " ".join(char)
            if char.isupper():
                swap_case_chars += char.lower()
            elif char.islower():
                swap_case_chars += char.upper()
    print("swap case chars -:",swap_case_chars)



rev("aWesome iS cODING")
