"""A Tic Tac Toe game application."""
import os
from logo import logo, logo2


def clear():
    """This function clears the console."""
    return os.system('clear')


def game_design(position):
    """This function prints the tic tac toe game structure."""
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


def game_status(player_positions, current_player):
    """This function checks for the status of the game"""
    winningCombinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for combo in winningCombinations:
        if all(playedCombo in player_positions[current_player] for playedCombo in combo):
            print(f"Player '{current_player}' won the game.")
            return True

    if len(player_positions['X']) + len(player_positions['O']) == 9:
        print("It's a Draw.")
        return True

    return False


def game():
    """This is the overall game functionalities."""
    print(logo)
    print('The displayed numbers in the logo above represents the game positions\n')

    current_player = 'X'

    gamePositions = [' ' for x in range(10)]

    # A list of game moves by each player
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
            # Replacing the position with the current player
            gamePositions[game_move] = current_player
            # tracking the game moves of each player
            playerPositions[current_player].append(game_move)

        if game_status(playerPositions, current_player):
            game_design(gamePositions)

            gameContinue = input("Do you want to play again? (Yes or No) ").title()

            if gameContinue == 'Yes':
                clear()
                game()
            elif gameContinue == 'No':
                game_start = False
                print('Thank you for using this application.')
            else:
                game_start = False
                print('Invalid response, Game Over.')
        else:
            game_design(gamePositions)

            # Switch players after every move
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'


game()
