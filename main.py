from game_controller import *

continue_game = True
continuee = True
sequence = Sequence()
game_controller= Game_controller()
while continue_game == True :
    game_controller.initialize_player()
    print("choisir la difficulté facile, moyen ou difficile")
    game_controller.level_difficulty()
    while continuee == True :
        game_controller.display_random()
        if game_controller.compare_value() == False :
            break
    play_again = input("Do you want to play again ?").lower()
    if play_again not in ["yes","y","oui","o"]:
        continue_game = False
