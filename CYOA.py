# class that represents inventory
class Inventory:
    def __init__(self):
        self.items = []


# class that keeps track of player data
class Player:
    def __init__(self,name):
        self.name = name
        self.hp = 10
        self.inventory = Inventory()


# this function runs the game loop
def game_run():
    is_user_playing = True
    print("Welcome to the game!")
    while is_user_playing == True:
        player = create_player()
        is_user_playing = False


# this function prompts the user for their name
# and then creates and returns the player
def create_player():
    player_name = input("What is your name?")
    player = Player(player_name)
    return player


game_run()

