import functions

word = functions.get_word()
guesses = -1
game_word = [char.upper() for char in word]
game_blanks = [" _ " for char in word]
game_done = [" _ " for char in word]

print(game_word)        # TODO Remove this code, for debugging only
print(game_blanks)      # TODO Remove this code, for debugging only

functions.start_screen()
print("Please press enter to begin!!")

while True:
    user = str(input(" -- > ")).casefold()
    print(word)     # TODO Remove this code, for debugging only
    if user.upper() in game_word:
        functions.game_screen(guesses)
        game_blanks[game_word.index(user.upper())] = user.upper()
        game_word[game_word.index(user.upper())] = " _ "
        print(game_blanks)

        if game_word == game_done:
            print("GAME OVER YOU WIN")
            # Create new screen as a celebration for winning
            break

    else:
        guesses += 1
        functions.game_screen(guesses)
        print(game_blanks)
        if guesses == 7:
            print("YOU LOSE")
            # If player loses, show the complete word.
            break
