text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
        'facilisis vitae semper at, dignissim vitae li')
words = text.split()
fin_words = []
for word in words:
    if word[-1] in ['.', ',']:
        word_new_p1 = word[:-1]
        word_new_p2 = word[-1]
        word_new = word_new_p1 + 'ing' + word_new_p2
    else:
        word_new = word + 'ing'
    fin_words.append(word_new)
new_text = ' '.join(fin_words)
print(new_text)

