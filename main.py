import random


def get_word():
    """
    Creates a list from almost every word in english and returns a random word.
    :return: returns a random word
    """
    words_list = []
    with open("only_words.txt", "r") as words:
        for word in words:
            words_list.append(word.strip())
    return words_list[random.randint(0, len(words_list))]


print(get_word())
