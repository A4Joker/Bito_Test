def even_len(given_string):
    if not isinstance(given_string, str):
        raise TypeError("Input must be a string")
    if not given_string.strip():
        return ""
    return ' '.join([word for word in given_string.split() if len(word) % 2 == 0])


even_len("I am a test string with even words")