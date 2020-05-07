from random import random


# class that represents inventory
class Inventory:
    def __init__(self):
        self.items = []

# class that keeps track of possibilities
class DecisionTree:
    def __init__(self):
        # this map represents how decision nodes are connected in the game
        game_map = {
            1: (2, 3, 4),
            2: (5, 6),
            3: (7, 8),
            4: (9, 10),
            5: (),
            6: (),
            7: (11, 12),
            8: (13, 14),
            9: (10, 14),
            10: (),
            11: (15, 16),
            12: (15, 16),
            13: (22),
            14: (17, 18, 23),
            15: (19, 20),
            16: (21, 22),
            17: (33, 34),
            18: (10),
            19: (),
            20: (24),
            21: (),
            22: (26, 27),
            23: (22),
            24: (25, 30),
            25: (32, 34),
            26: (31),
            27: (32, 34),
            28: (33, 34),
            30: (34),
            31: (34),
            32: (),
            33: (),
            34: (),
        }
        # rng node map
        rng_node_map = {
            "corona": (14, 21, 31),
            "police": (17, 28),
            "mugged": (25, 27),
        }
# class that represents a single possible decision
class DecisionTreeNode:
    def __init__(self,what_happened):
        self.what_happened = what_happened
        connections = {}

# class to keep track of rng
class RNG:
    def __init__(self,rng_type,rng_odds):
        self.rng_type = rng_type
        self.rng_odds = rng_odds
    # This is a function that creates an outcomes based on odds
     def get_negative_event_outcome(self):
        random_event_number = random()
        if random_event_number > self.rng_odds:
            return False
        else:
            return True


# class that keeps track of player data
class Player:
    def __init__(self,name):
        self.name = name
        self.inventory = Inventory()


# this function returns a dictionary that maps a string to a decimal value
# the strings represent different types of rng and the decimal value represents the probability
def create_rng_odds():
    rng_dict = {"corona" : .5,"police" : .66,"mugged" : .25}
    return rng_dict



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

