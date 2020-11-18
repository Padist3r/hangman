# This module was used to write only the basic words to a new file.
# It removed all words that contained numbers or other characters.
# Also removed any names or any word starting with a capital letter.

words = []
with open("words.txt", "r") as all_words:
    for word in all_words:
        if word.strip().isalpha() and not word.strip()[0].isupper():
            words.append(word.strip())

with open("only_words.txt", "w") as only_words:
    for i in words:
        print(i, file=only_words)
