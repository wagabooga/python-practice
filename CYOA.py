class Inventory:
    # class that represents inventory
    def __init__(self):
        self.items = []


class Player:
    #class that keeps track of player data
    def __init__(self,name):
        self.name = name
        self.hp = 10
        self.inventory = Inventory()


def game_run():
    is_user_playing = True
    while is_user_playing == True:
        #the game runs inside of this loop
        print("Welcome to the game")
        is_user_playing = False

game_run()