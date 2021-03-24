"""A Tic Tac Toe game application."""
import os
from logo import logo, logo2


# Clear console
def clear():
    return os.system('clear')


def game_design(position):
    print("\n"
          "         |         |         \n"
          f"    {position[1]}    |    {position[2]}    |    {position[3]}  \n"
          "_________|_________|_________\n"
          "         |         |         \n"
          f"    {position[4]}    |    {position[5]}    |    {position[6]}  \n"
          "_________|_________|_________\n"
          "         |         |         \n"
          f"    {position[7]}    |    {position[8]}    |    {position[9]}  \n"
          "         |         |         \n"
          "\n")


def game():
    print(logo)
    print('The displayed numbers in the logo above represents the game positions\n')

    current_player = 'X'

    gamePositions = [' ' for x in range(10)]

    playerPositions = {'X': [], 'O': []}

    game_start = True
    while game_start:

        try:
            print(f"It's your move, player '{current_player}'")
            game_move = int(input('What position is your game move? '))
        except ValueError:
            print('Input must be an integer.\n')

        clear()
        print(logo2)
        if game_move < 1 or game_move > 9:
            print('Invalid input, must be between 1 and 9. Play again\n')
        if gamePositions[game_move] != ' ':
            print('Position occupied, Play again\n')
        else:
            gamePositions[game_move] = current_player
            playerPositions[current_player].append(game_move)

            # Switch players after every move
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

        game_design(gamePositions)


game()
