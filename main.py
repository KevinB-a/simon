import time

from sequence import *

from game_controller import *

sequence = Sequence()
game_controller= Game_controller()
game_controller.initialize_player()
game_controller.level_difficulty()
game_controller.display_random()
game_controller.add_player_entry()
for element in sequence.random_list :
    if element == game_controller.add_player_entry() :
        print("vous avez le bon nombre")
