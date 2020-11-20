import functions

# TODO Rewrite the main code so it matches all characters of character (x)
#  when the user types in (x). Code is also hard to read in main function.


def hangman():
    word = functions.get_word()
    guesses = -1
    game_word = [char.upper() for char in word]
    game_blanks = [" _ " for char in word]
    game_done = [" _ " for char in word]

    functions.start_screen()
    print("Please press enter to begin!!")

    while True:
        user = str(input(" -- > ")).casefold()
        if user.upper() in game_word:
            functions.game_screen(guesses)
            game_blanks[game_word.index(user.upper())] = user.upper()
            game_word[game_word.index(user.upper())] = " _ "
            print(game_blanks)

            if game_word == game_done:
                functions.win_screen()
                break

        else:
            guesses += 1
            functions.game_screen(guesses)
            print(game_blanks)
            if guesses == 7:
                functions.lose_screen(word.upper())
                break


if __name__ == '__main__':
    while True:
        hangman()
        play_again = input("Would you like to play again? Y/N --> ").casefold()

        yn = ["y", "n"]
        if play_again == "y":
            continue
        elif play_again == "n":
            break
        else:
            while play_again not in yn:
                play_again = input("Please enter a valid response... "
                                   "Would you like to play again? Y/N --> ")
