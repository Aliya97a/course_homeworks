def char_frequency(text):
    text = text.lower()
    frequency = {}

    for i in text:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    return frequency


text = "Привет!"
# print(char_frequency(text))
print(char_frequency(text) == {'п': 1, 'р': 1, 'и': 1, 'в': 1, 'е': 1, 'т': 1, '!': 1})
text = "КАК дела!"
print(char_frequency(text) == {'к': 2, 'а': 2, ' ': 1, 'д': 1, 'е': 1, 'л': 1, '!': 1})
text = "1997 years "
print(char_frequency(text) == {'1': 1, '9': 2, '7': 1, ' ': 2, 'y': 1, 'e': 1, 'a': 1, 'r': 1, 's': 1})
