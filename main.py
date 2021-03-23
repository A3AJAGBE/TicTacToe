"""A Tic Tac Toe game application."""

from logo import logo

print(logo)
print('Use the display numbers to play in your preferred position\n')
# player_1 = int(input('What position? '))
# print(player_1)


def game_design(position):
    print("\n"
          "         |         |         \n"
          f"    {1}    |    {2}    |    {3}  \n"
          "_________|_________|_________\n"
          "         |         |         \n"
          f"    {4}    |    {5}    |    {6}  \n"
          "_________|_________|_________\n"
          "         |         |         \n"
          f"    {7}    |    {8}    |    {9}  \n"
          "         |         |         \n"
          "\n")


