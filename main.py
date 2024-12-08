# Run an instance of Fox Game!
from src.FoxGame import *

foxgame = FoxGame()
foxgame.print_board()
print(foxgame.get_total_letters_left())
foxgame.check_game_end()
