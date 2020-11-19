import random
import os


def get_word():
    """
    Creates a list from almost every word in english and returns a random word.
    :return: returns a random word
    """
    with open("only_words.txt", "r") as words:
        words_list = [word.strip() for word in words]
    return words_list[random.randint(0, len(words_list))]


def clear():
    """Clears the console"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def game_screen(wrong_guesses):
    """Controls the game screen"""
    screen_visual = (
        """
        |---------
        |     |
        |
        |
        |
        |
        |
        |____________
        """,
        """
        |---------
        |     |
        |     0
        |
        |
        |
        |
        |____________
        """,
        """
        |---------
        |     |
        |     0
        |     |
        |
        |
        |
        |____________
        """,
        """
        |---------
        |     |
        |     0
        |    \\|
        |
        |
        |
        |____________
        """,
        """
        |---------
        |     |
        |     0
        |    \\|/
        |
        |
        |
        |____________
        """,
        """|---------
        |     |
        |     0
        |    \\|/
        |     |
        |
        |
        |____________
        """,
        """
        |---------
        |     |
        |     0
        |    \\|/
        |     |
        |    / 
        |
        |____________
        """,
        """
        |---------
        |     |
        |     0
        |    \\|/
        |     |
        |    / \\
        |  GAME OVER
        |____________
        """
    )
    clear()
    print(screen_visual[wrong_guesses])


def start_screen():
    print(
        """
        #####################################################################
        #####################################################################
        ######                                                         ######
        ######                         HANGMAN                         ######
        ######                                                         ######
        #####################################################################
        #####################################################################
        """
    )