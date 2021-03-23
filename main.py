"""A Tic Tac Toe game application."""

from logo import logo

print(logo)
print('Use the display numbers to play in your preferred position\n')


def game_design(position):
    print("\n"
          "         |         |         \n"
          f"    {position[0]}    |    {position[1]}    |    {position[2]}  \n"
          "_________|_________|_________\n"
          "         |         |         \n"
          f"    {position[3]}    |    {position[4]}    |    {position[5]}  \n"
          "_________|_________|_________\n"
          "         |         |         \n"
          f"    {position[6]}    |    {position[7]}    |    {position[8]}  \n"
          "         |         |         \n"
          "\n")


game_start = True
while game_start:
    player_1 = input('What position? ')

    if player_1.isdigit():
        if int(player_1) < 1 or int(player_1) > 9:
            print('Invalid input, must be between 1 and 9.\n')
        else:
            print(player_1)
            game_start = False
    else:
        print('Input must be an integer.\n')
