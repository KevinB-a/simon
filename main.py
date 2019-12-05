from game_controller import *

continuee = True
sequence = Sequence()
game_controller= Game_controller()
game_controller.initialize_player()
game_controller.level_difficulty()
while continuee == True :
    game_controller.display_random()
    if game_controller.compare_value() == False :
        break
