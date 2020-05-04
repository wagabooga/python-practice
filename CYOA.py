from random import random


# class that represents inventory
class Inventory:
    def __init__(self):
        self.items = []

# class that keeps track of possibilities
class DecisionTree:
    def __init__(self):
        print("helloworld")


# class that represents a single possible decision
class DecisionTreeNode:
    def __init__(self,what_happened):
        self.what_happened = what_happened


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

