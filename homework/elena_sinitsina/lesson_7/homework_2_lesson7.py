def print_words(words):
    for key, value in words.items():
        print(key * value)


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
print_words(words)
