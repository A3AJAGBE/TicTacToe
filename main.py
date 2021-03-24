"""A Tic Tac Toe game application."""

from logo import logo

print(logo)
print('Use the display numbers to play in your preferred position\n')


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
    current_player = 'X'

    gamePositions = [' ' for x in range(10)]

    playerPositions = {'X': [], 'O': []}

    game_start = True
    while game_start:

        try:
            game_move = int(input('What position is your game move? '))
        except ValueError:
            print('Input must be an integer.\n')

        if game_move < 1 or game_move > 9:
            print('Invalid input, must be between 1 and 9.\n')
        elif gamePositions[game_move] != ' ':
            print('Position occupied, Play again\n')
        else:
            gamePositions[game_move] = current_player
            playerPositions[current_player].append(game_move)

        game_design(gamePositions)


game()
