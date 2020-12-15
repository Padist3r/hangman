import functions


def hangman():
    word = functions.get_word()
    guesses = -1
    game_word = [char.upper() for char in word]
    game_word_display = [" _ " for char in word]
    game_done = [" _ " for char in word]
    wrong_guesses = []

    functions.start_screen()
    print("Please press enter to begin!!")

    while True:
        user = str(input(" -- > ")).casefold()

        # This `if` statement makes sure that the initial value of -1 doesn't
        # get passed on if the user gets a correct guess on their first turn
        if user.upper() in game_word:
            if guesses == -1:
                guesses = 0
            functions.game_screen(guesses)

            for i in range(len(game_word)):
                if user.upper() == game_word[i]:
                    # Updates the game to display the newly discovered letters
                    game_word_display[i] = user.upper()
                    # Removes letters that have been found from `game_word`
                    game_word[i] = " _ "

            print(game_word_display)
            print(f"Wrong guesses: {wrong_guesses}")

            # When all the letters in `game_word` are found and removed
            # `game_word` will equal `game_done`
            if game_word == game_done:
                functions.win_screen()
                break

        else:

            if user not in wrong_guesses and user.isalpha():
                wrong_guesses.append(user.upper())

            guesses += 1
            functions.game_screen(guesses)
            print(game_word_display)
            print(f"Wrong guesses: {wrong_guesses}")
            if guesses == 7:
                functions.lose_screen(word.upper())
                break


if __name__ == '__main__':
    play_game = True
    while play_game:
        hangman()
        play_again = input("Would you like to play again? Y/N --> ").casefold()

        if play_again == "y":
            play_game = True
        elif play_again == "n":
            play_game = False
        else:
            while play_again not in "yn":
                play_again = input("Please enter a valid response... "
                                   "Would you like to play again? "
                                   "Y/N --> ").casefold()
                if play_again == "y":
                    play_game = True
                elif play_again == "n":
                    play_game = False
